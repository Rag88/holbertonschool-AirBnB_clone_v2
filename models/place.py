#!/usr/bin/python3
"""
Place Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    A place to stay
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if (getenv('HBN_TYPE_STORAGE') == 'db'):
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="places_amenities")
    else:
        @property
        def reviews(self):
            from models import storage
            all_reviews = storage.all(Review)

            new_list = []
            for review in all_reviews:
                if (review.id == self.id):
                    new_list.append(review)
            return new_list

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            all_amenities = storage.all(Amenity)

            new_list = []
            for amenity in all_amenities:
                if (amenity.place_id == self.id):
                    new_list.append(amenity)
            return new_list

        @amenities.setter
        def amenities(self, obj=None):
            if (type(obj).__name__ == "Amenity"):
                self.amenity_ids.append(obj.id)
