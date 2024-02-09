#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
import os
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """Representation of a user """
    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if kwargs:
            pwd = kwargs.pop('password', None)
            if pwd:
                # Hash the password using MD5
                secure = hashlib.md5()
                secure.update(pwd.encode("utf-8"))
                secure_password = secure.hexdigest()
                kwargs['password'] = secure_password

        super().__init__(*args, **kwargs)
