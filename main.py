from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import select

from .db import init_db, SessionDep
from .models import Job, JobPublic, JobCreate

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

@app.post("/api/jobs", response_model=JobPublic)
async def create_job(job: JobCreate, session: SessionDep):
    db_job = Job.model_validate(job)

    session.add(db_job)
    await session.commit()
    await session.refresh(db_job)

    return db_job