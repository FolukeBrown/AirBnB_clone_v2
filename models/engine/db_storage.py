#!/usr/bin/python3

"""
Class for the Database Storage
"""
from os import getenv
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """Database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates engine that links to database"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        dbb = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")

        db_engine = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, dbb)
        self.__engine = create_engine(db_engine, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self._engine)

    def all(self, cls=None):
        """
        Queries database and returns a dictionary of objects
        """
        if not self.__session:
            self.reload()

        classes = [State, City, Place, User, Review, Amenity]
        res = {}

        if cls is not None:
            obj = self.__session.query(cls).all()
            for k in obj:
                key = k.__class.__name__ + '.' + k.id
                res[key] = k
        else:
            for clss in classes:
                obj = self.__session.query(clss).all()
                for k in obj:
                    key = k.__class.__name__ + '.' + k.id
                    res[key] = k
        return res

    def new(self, obj):
        """
        Adds object to the current database
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes object from the current database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates tables in the database
        """
        Base.metadata.create_all(self.__engine)
        # CREATING SESSION
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        session_scoped = scoped_session(session_factory)
        self.__session = Session()
