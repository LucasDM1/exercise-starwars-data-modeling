import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username=Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password=Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year= Column(Integer)
    gender=Column(String(250))
    hair_color=Column(String(250))
    height= Column(Integer)
    eye_color=Column(String(250))

class favorite_Character(Base):
    __tablename__='favorite_characters'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    character = relationship(Character)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate=Column(String(250))
    population= Column(Integer)
    orbital_period= Column(Integer)
    rotation_period= Column(Integer)
    diameter= Column(Integer)
    
class favorite_Planet(Base):
    __tablename__='favorite_planets'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    planet = relationship(Planet)


# class Address(Base):
#     __tablename__ = 'address'
#     Here we define columns for the table address.
#     Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')