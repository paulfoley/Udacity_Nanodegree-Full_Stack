# Create Restaurant Classes

## Imports
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
	__tablename__ = 'Restaurant'
	name = Column(String(250), nullable = False)
	id = Column(Integer, primary_key = True)

	@property
	def serialize(self):
		""" Return object data in easily serializeable format """
		return {
			'name': self.name,
			'id': self.id,
		}

class MenuItem(Base):
	__tablename__ = 'Menu_Item'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('Restaurant.id'))
	restaurant = relationship(Restaurant)

	@property
	def serialize(self):
		""" Returns object data in easily serializeable format """
		return {
			'name': self.name,
			'description': self.description,
			'id': self.id,
			'price': self.price,
			'course': self.course,
		}

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)