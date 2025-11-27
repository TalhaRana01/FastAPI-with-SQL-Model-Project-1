from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(BASE_DIR)

db_path = os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
  SQLModel.metadata.create_all(engine)
  
def get_session():
   with Session(engine) as session:
     yield session
     
SessionDependency = Annotated[Session, Depends(get_session)]