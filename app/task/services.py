from sqlmodel import Session, select
from app.task.model import Task
from app.database.config import engine
from fastapi import HTTPException


# Create Task
def create_task(title: str, content:str):
  task = Task(title=title, content=content)
  with Session(engine) as session:
    session.add(task)
    session.commit()
    session.refresh()
    return task 
  
# Get Task by ID
def get_task_by_id(task_id: int):
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    return task
  
# Update Task
def update_task(task_id: int, title: str, content: str):
  with Session(engine) as session:
    task = session.get(task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    task.title = title
    task.content = content
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
  
# Update Partial Task
def patch_task(task_id: int, title:str | None = None, content: str | None = None):
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    if title is not  None:
      task.title = title
    if content is not None:
      task.content = content
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
  
# Delete Task 
def delete_task(task_id: int):
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    session.add(task)
    session.commit()
    return task
      
    
  