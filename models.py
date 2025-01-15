from sqlmodel import SQLModel, Field

class JobBase(SQLModel):
    title: str = Field(index=True)
    description: str = Field(index=True)
    salary: float | None = Field(default=None, index=True)

class Job(JobBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class JobPublic(JobBase):
    id: int

class JobCreate(JobBase):
    pass
