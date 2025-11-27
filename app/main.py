from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.config import create_tables
from app.task.services import *

@asynccontextmanager
async def lifespan(app:FastAPI):
  create_tables()
  yield
  
app = FastAPI(lifespan=lifespan)
  
