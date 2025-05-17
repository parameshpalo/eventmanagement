from fastapi import FastAPI
import models
from routers import events,guests,users
from db import Base,get_db,engine

models.Base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(events.router)
app.include_router(guests.router)
app.include_router(users.router)

app.get("/")
def root():
  return "hello world"