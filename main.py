from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import select

from .db import init_db, SessionDep
from .models import Job, JobPublic, JobCreate, JobUpdate

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server is shutting down..")
    

app = FastAPI(lifespan=lifespan)

@app.get("/api/jobs", response_model=list[JobPublic])
async def read_jobs(session: SessionDep):
    jobs = await session.exec(select(Job))
    return jobs

@app.get("/api/jobs/{job_id}", response_model=JobPublic)
async def read_job(job_id: int, session: SessionDep):
    job = await session.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@app.post("/api/jobs", response_model=JobPublic)
async def create_job(job: JobCreate, session: SessionDep):
    db_job = Job.model_validate(job)

    session.add(db_job)
    await session.commit()
    await session.refresh(db_job)

    return db_job

@app.patch("/api/jobs/{job_id}", response_model=JobPublic)
async def update_job(job_id: int, job: JobUpdate, session: SessionDep):
    job_db = await session.get(Job, job_id)
    if not job_db:
        raise HTTPException(status_code=404, detail="Job not found")
    job_data = job.model_dump(exclude_unset=True)
    job_db.sqlmodel_update(job_data)
    session.add(job_db)
    await session.commit()
    await session.refresh(job_db)
    return job_db

@app.delete("/api/jobs/{job_id}")
async def delete_job(job_id: int, session: SessionDep):
    job = await session.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    await session.delete(job)
    await session.commit()
    return { "ok": True }