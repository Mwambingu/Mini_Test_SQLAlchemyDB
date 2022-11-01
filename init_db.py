#!/usr/bin/python3

from base import session, engine
from tables import User, Post, Tag
from data import usernames, posts, tags, passwords, randM


def create_user(name, pass_key):
  for i in usernames:
    session.add(User(username = randM(name), password = randM(pass_key)))
  session.commit()

def create_post(post):
  user_objs = session.query(User).all()
  for i in user_objs:
    for p in range(3):
      session.add(Post(user_id = i.id, post = randM(posts)))
  session.commit()

def create_tags(tag_name):
  for i in tags:
    session.add(Tag(tag = i))
  session.commit()

create_user(usernames, passwords)
create_tags(tags)
create_post(posts)