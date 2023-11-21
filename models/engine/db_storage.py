#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

classes = {"Amenity": Amenity, "City": City, "Place": Place,
        "Review": Review, "State": State, "User": User}


class DBStorage:
    """DataBase Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initialises a DBStorage class instance"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns dictionary of all types of objects of DB"""
        dictionary = {}
        if cls:
            dictionary = {obj.__class__.__name__+"."+obj.id: obj for obj in
                    self.__session.query(classes[cls]).all()}
        else:
            for quer in Base.__subclasses__():
                table = self.__session.query(quer).all()
                for obj in table:
                    dictionary[obj.__class__.__name__+"."+obj.id] = obj
        return dictionary

    def new(self, obj):
        """adds object to the current DB session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current DB session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current DB session"""
        self.__session.delete(obj)


    def reload(self):
        """creates all tables in DB, creates the current DB session"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        self.__session.close()
