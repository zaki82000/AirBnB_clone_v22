#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )

    if getenv('HBNB_ENV') == 'test':
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        class_name = (User, State, City, Amenity, Place, Review)
        output = {}

        if cls:
            for obj in self.__session.query(cls).all():
                output[f'{obj.__class__.__name__}.{obj.id}'] = obj
        elif cls in class_name:
            for obj in self.__session.query(cls).all():
                output[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return output

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        )
        self.__session = session()
