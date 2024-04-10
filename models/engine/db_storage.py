#!/usr/bin/python3
"""New engine DBStorage"""
import json
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

classes = {
               'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }


class DBStorage:
    """Interacts with the MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        environment = getenv('HBNB_ENV')
        # Create the engine
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        # Drop all tables if environment is set to 'test'
        if environment == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name."""
        obj_dict = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = f'{cls.__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = f'{cls.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables from the database and recreate the session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Call remove() method"""
        self.__session.remove()
