#!/usr/bin/python3

from base import session, engine
from tables import User, Post, Tag
from data import usernames, posts, tags, passwords, randM
from sqlalchemy import text

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

def link_tags():
  post_ids_list = []
  tag_ids_list = []
  post_objs_list = session.query(Post).all()
  tag_objs_list = session.query(Tag).all()

  for post_obj in post_objs_list:
    temp_list = tag_objs_list.copy()
    for i in range(2):
      tag_obj = randM(temp_list)
      temp_list.remove(tag_obj)
      post_obj.tags.append(tag_obj)
  
  session.commit()

  
  # for tag_obj in tag_objs_list:
  #   tag_ids_list.append(tag_obj.id)
  
  # print("*****printing post ids******")
  # for post_id in post_ids_list:
  
  # print("*****printing tag ids******")
  # for tag_id in tag_ids_list:

def get_posts():
  post_objs_list = session.query(Post).all()
  for post_obj in post_objs_list:
    print(f"***Username: {post_obj.user.username}***")
    print(f"Post:{post_obj.post}")
    for tag_obj in post_obj.tags:
      print(f"Tag:{tag_obj.tag}", end=" ")
    print("")
    print("")

def drop_all_tables():
  """
  
  """
  sql = text('drop tables if exists association_table, posts, tags, user;')
  engine.execute(sql)
  


#Initializing the DB with dummy data
create_user(usernames, passwords)
create_tags(tags)
create_post(posts)

#linking tags and posts using association_table.
link_tags()

#Getting posts with the users plus tags.
get_posts()

#Drop Tables after testing with dummy data.
drop_all_tables()