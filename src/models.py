import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    usermame = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    favorito = relationship("Favorito")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    status = Column(String(200), nullable=False)
    species = Column(String(200), nullable=False)
    gender = Column(String(200), nullable=False)
    origin = Column(String(200), nullable=False)
    episodio= relationship("Episode")
    favorito = relationship("Favorito")
    location =relationship("Location")


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    dimension = Column(String(200), nullable=False)
    residents = Column(String(200), ForeignKey("character.name"))
 

class Episode(Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    air_date = Column(String(200), nullable=False)
    episode = Column(String(200), nullable=False)
    character=Column(String(200),ForeignKey("character.name"))

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    personaje = Column(String(200),ForeignKey("character.name"))
    user = Column(String(200),ForeignKey("user.name"))







render_er(Base, 'diagram.png')
