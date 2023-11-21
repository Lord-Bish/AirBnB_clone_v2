#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                backref="state", cascade="all, delete-orphan")
    else:
        name = ""
        @property
        def cities(self):
            LCity = models.storage.all(models.classes['City']).values()
            return [city for city in LCity if city.state_id == self.id]
