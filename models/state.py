#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import getenv, environ
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
    class State that inherets from BaseModel
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if (getenv('HBN_TYPE_STORAGE') == 'db'):
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            all_cities = storage.all(City)

            new_list = []
            for city in all_cities:
                if (city.states_id == self.id):
                    new_list.append(city)
            return new_list
