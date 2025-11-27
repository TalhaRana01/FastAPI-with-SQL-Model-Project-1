from sqlmodel import Session, select
from app.task.model import Task, TaskOut, TaskUpdate, TaskPatch, TaskCreate
from app.database.config import engine
from fastapi import HTTPException


# Create Task
def create_task(new_task : TaskCreate) -> TaskOut:
  task = Task(title=new_task.title, content=new_task.content)
  with Session(engine) as session:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task 
  
# Get All Tasks
def get_tasks()-> list[TaskOut]:
  with Session(engine) as session:
    statement = select(Task)
    tasks = session.exec(statement).all()
    if not tasks:
      raise HTTPException(status_code=404, detail="Task not found")
    return tasks
      
  
# Get Task by ID
def get_task_by_id(task_id: int) -> TaskOut:
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    return task
  
# Update Task
def update_task(task_id: int, new_task: TaskUpdate):
  with Session(engine) as session:
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
def patch_task(task_id: int, new_task: TaskPatch)-> TaskOut:
  with Session(engine) as session:
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
def delete_task(task_id: int):
  with Session(engine) as session:
    task = session.get(Task, task_id)
    if not task:
      raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"Ok": True}
      
    
  