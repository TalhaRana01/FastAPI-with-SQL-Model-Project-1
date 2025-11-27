from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.config import create_tables
from app.task.services import *

@asynccontextmanager
async def lifespan(app:FastAPI):
  create_tables()
  yield
  
app = FastAPI(lifespan=lifespan)

# Create Task
@app.post("/task")
def task_create(new_task: dict):
  task = create_task(title=new_task["title"], content=new_task["content"])
  return task


# Get Single Task
@app.get("/task{task_id}")
def get_task(task_id: int):
  task = get_task_by_id(task_id)
  return task

# Update Task
@app.put("/task/{task_id}")
def task_update(task_id: int, new_task: dict):
  task = update_task(task_id, title=new_task["title"])
  return task

# Partial Update Task
@app.patch("/task/{task_id}")
def patch_task_update(task_id: int, new_task: dict):
  task = patch_task(task_id, title=new_task.get("title"), content=new_task.get("content"))
  return task


# Delete Task
@app.delete("/task/{task_id}")
def task_delete(task_id: int):
  task = delete_task(task_id)
  return task
