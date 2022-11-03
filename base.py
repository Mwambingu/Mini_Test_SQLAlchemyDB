#!/usr/bin/python3
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from uuid import uuid4
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("mysql+mysqldb://root:root@localhost/test_many", echo=False, pool_pre_ping=True)

session_factory = sessionmaker(bind=engine, expire_on_commit=False)
session = scoped_session(session_factory)

Base = declarative_base()

class BaseModel():

  id = Column(String(60), primary_key=True)
  created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

  def __init__(self, *args, **kwargs):
    self.id = str(uuid4())
    self.created_at = datetime.utcnow()
    if kwargs:
      self.__dict__.update(kwargs)