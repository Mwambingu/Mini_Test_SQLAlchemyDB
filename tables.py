#!/usr/bin/python3
"""
Contains the association table, User, Post and Tag models.
For setting up the db objects and their relationships.
"""
from base import BaseModel, Base, engine
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table(
    "association_table",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id")),
    Column("tag_id", ForeignKey("tags.id")),
)


class User(BaseModel, Base):
    """Class that instantiates a User"""
    __tablename__ = "user"
    username = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)

    posts = relationship("Post", backref="user", cascade="all, delete")


class Post(BaseModel, Base):
    """Class that instantiates a Post"""
    __tablename__ = "posts"

    user_id = Column(String(60), ForeignKey("user.id"), nullable=False)
    post = Column(String(512), nullable=False)
    tags = relationship("Tag", secondary=association_table)


class Tag(BaseModel, Base):
    """Class that instantiates a Tag"""
    __tablename__ = "tags"

    tag = Column(String(16), nullable=False)


Base.metadata.create_all(engine)
