#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                "City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """GETTER ATTRIBUTE"""
            from models.city import City
            from models.engine.file_storage import FileStorage
            fs = FileStorage()
            cities = fs.all(City)
            city_obj = []
            for city in cities.values():
                if city.state_id == self.id:
                    city_obj.append(city)
            return city_obj
