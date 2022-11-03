#!/usr/bin/python3
"""
Contains the BaseModel that is the base class for all other models.
Setups the engine and table structure for sqlalchemy.
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from uuid import uuid4
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(
    "mysql+mysqldb://root:root@localhost/test_many",
    echo=False,
    pool_pre_ping=True)

session_factory = sessionmaker(bind=engine, expire_on_commit=False)
session = scoped_session(session_factory)

Base = declarative_base()


class BaseModel():
    """The base class for all models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatiates the model"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        if kwargs:
            self.__dict__.update(kwargs)
