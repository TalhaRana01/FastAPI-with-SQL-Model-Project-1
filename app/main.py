from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.config import create_tables, SessionDependency
from app.task.services import *
from app.task.model import*


@asynccontextmanager
async def lifespan(app:FastAPI):
  create_tables()
  yield
  
app = FastAPI(lifespan=lifespan)

# Create Task
@app.post("/task", response_model=TaskOut) 
def task_create(session: SessionDependency, new_task: TaskCreate):
  task = create_task(session, new_task)
  return task


# Get All Task
@app.get("/task", response_model=list[TaskOut])
def get_all_task(session: SessionDependency):
  tasks = get_tasks(session)
  return tasks


# Get Single Task
@app.get("/task{task_id}")
def get_task(session: SessionDependency, task_id: int):
  task = get_task_by_id(session, task_id)
  return task


# Update Task
@app.put("/task/{task_id}")
def task_update(session: SessionDependency, task_id: int, new_task: TaskUpdate):
  task = update_task(session, task_id, new_task)
  return task


# Partial Update Task
@app.patch("/task/{task_id}")
def patch_task_update(session: SessionDependency, task_id: int, new_task: TaskPatch):
  task = patch_task(session, task_id, new_task)
  return task


# Delete Task
@app.delete("/task/{task_id}")
def task_delete(session: SessionDependency, task_id: int):
  task = delete_task(session, task_id)
  return task
