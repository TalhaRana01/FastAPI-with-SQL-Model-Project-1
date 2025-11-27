from sqlmodel import Session, select
from app.task.model import Task, TaskOut, TaskUpdate, TaskPatch, TaskCreate
from app.database.config import engine
from fastapi import HTTPException


# Create Task
def create_task(session:Session, new_task : TaskCreate) -> TaskOut:
  task = Task(title=new_task.title, content=new_task.content)
  session.add(task)
  session.commit()
  session.refresh(task)
  return task 
  
  
# Get All Tasks
def get_tasks(session:Session)-> list[TaskOut]:
    statement = select(Task)
    tasks = session.exec(statement).all()
    if not tasks:
      raise HTTPException(status_code=404, detail="Task not found")
    return tasks
  
      
  
# Get Task by ID
def get_task_by_id(session:Session, task_id: int) -> TaskOut:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    return task
  
  
# Update Task
def update_task(session:Session, task_id: int, new_task: TaskUpdate):
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    task.title = new_task.title
    task.content = new_task.content
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
  
  
# Update Partial Task
def patch_task(session:Session, task_id: int, new_task: TaskPatch)-> TaskOut:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    if new_task.title is not  None:
      task.title = new_task.title
    if new_task.content is not None:
      task.content = new_task.content
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
  
  
# Delete Task 
def delete_task(session:Session, task_id: int):
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"Ok": True}
  
      
    
  