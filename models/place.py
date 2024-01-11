#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models.user import User
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship(
                "Review", backref="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            """GETTER ATTRIBUTE"""
            from models.review import Review
            from models.engine.file_storage import FileStorage
            fs = FileStorage()
            reviews = fs.all(Review)
            rev_obj = []

            for rev in reviews.values():
                if rev.place_id == self.id:
                    rev_obj.append(rev)
                    return rev_obj
