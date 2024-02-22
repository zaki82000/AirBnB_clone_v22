#!/usr/bin/python3
""" User module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Definition of the User class """
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all,delete", backref="user")
        reviews = relationship("Review", cascade="all,delete", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''