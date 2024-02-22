#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullabel = False)
    password = Column(String(128), nullabel = False)
    first_name = Column(String(128), nullabel = False)
    last_name = Column(String(128), nullabel = False)
