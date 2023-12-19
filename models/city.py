#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey

class City(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(128), nullable=False, ForeignKey('states_id')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
