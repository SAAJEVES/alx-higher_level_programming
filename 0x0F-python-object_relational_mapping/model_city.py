#!/usr/bin/python3
'''
Python file similar to model_state.py named model_city.py
that contains the class definition of a City
'''

from model_state import Base, State
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey='states.id')

    state = relationship('State', back_populate="cities")


State.cities = relation('City', backpopulate="state")
