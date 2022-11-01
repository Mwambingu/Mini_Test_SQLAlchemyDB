#!/usr/bin/python3
from base import BaseModel, Base, engine
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
  __tablename__ = "user"
  username = Column(String(60), nullable=False)
  password = Column(String(60), nullable=False)
  
  posts = relationship("Post", backref="user", cascade="all, delete")

class Post(BaseModel, Base):
  __tablename__ = "posts"

  user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
  post = Column(String(512), nullable=False)

class Tag(BaseModel, Base):
  __tablename__ = "tags"

  tag = Column(String(16), nullable=False)


Base.metadata.create_all(engine)