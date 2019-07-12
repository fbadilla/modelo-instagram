import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    # Here we define columns for python3 src/models.pythe table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    user = Column(String(10), nullable=False)
    sitio_web = Column(String(30), nullable=False)
    email = Column(String(20), nullable=False)
    phone = Column(String(12), )

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    date = Column(String(250))
    users_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

class Coments(Base):
    __tablename__ = 'coments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    date = Column(String(250))
    users_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_post = relationship(Posts)
class Follows(Base):
    __tablename__ = 'follows'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(String(250))
    userW = relationship(Users)
    userF = relationship(Users)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')