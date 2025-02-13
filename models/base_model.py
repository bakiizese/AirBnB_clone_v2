#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import sqlalchemy

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    if models.storage_t == "db":
        id = Column(String(60), unique=True, nullable=False,
                    primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        '''to create new or existing instance'''
        if kwargs is not None:
            for key in kwargs:
             #   print('{} = {}'.format(key, kwargs[key]))
                self.__dict__[key] = kwargs[key]
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        return dictionary"""
        mydict = self.__dict__.copy()
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        mydict["__class__"] = self.__class__.__name__

        return mydict

    def delete(self):
        """delete current"""
        models.storage.delete(self)
