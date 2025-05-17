from db import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime

class User(Base):
  __tablename__='users_table'
  user_id=Column(Integer,primary_key=True,nullable=False)
  user_name= Column(String(100),nullable=False)
  user_email=Column(String(100),nullable=False)
  password=Column(String(100),nullable=False)

class Event(Base):
  __tablename__='events_table'

  event_id = Column(Integer,primary_key=True,nullable=False)
  event_name =Column(String(100),nullable=False)
  event_organiser=Column(Integer,ForeignKey("users_table.user_id"),nullable=False)
  event_date = Column(DateTime,nullable=False)
  event_location = Column(String(100),nullable=False)

class Guest(Base):
  __tablename__='guests_table'
  guest_id=Column(Integer,primary_key=True,nullable=False)
  guest_name=Column(String(100),nullable=False)
  guest_email=Column(String(100),nullable=False)
  event_id=Column(Integer,ForeignKey("events_table.event_id"),nullable=False)
  



