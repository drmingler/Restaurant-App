import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    name = Column(String(200), nullable= False)

    picture = Column(String(300))

    email = Column(String(200), nullable= False)


class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable=False)

    id = Column(Integer, primary_key=True)

    users_id = Column(Integer,ForeignKey('users.id'))

    users = relationship(Users)


class MenuItem(Base):
    __tablename__ = 'menuitem'

    name = Column(String(80), nullable=False)

    id = Column(Integer, primary_key=True)

    course = Column(String(250))

    description = Column(String(250))

    price = Column(Integer)

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    restaurant = relationship(Restaurant)

    user_id = Column(Integer,ForeignKey('users.id'))

    users = relationship(Users)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'course': self.course,
            'description': self.description,
            'price': self.price,
        }

##To point to the database we will be using
engine = create_engine('sqlite:///restflaskwithusers.db')

Base.metadata.create_all(engine)
