#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column,String



class City(BaseModel):
    __tablename__ = 'cities'
    name = Column(String(128), nullabel = False)
    state_id = Column(String(60), nullabel = False, ForeignKey = ('states.id'))
    