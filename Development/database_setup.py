from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Coders(Base):
    __tablename__ = 'coders'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
        }


class Programs(Base):
    __tablename__ = 'programs'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    filename = Column(String(250), nullable=False)
    coder_id = Column(Integer, ForeignKey('coders.id'))
    coders = relationship(Coders)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'filename': self.filename,
        }


class Bugs(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    program_id = Column(Integer, ForeignKey('programs.id'))
    programs = relationship(Programs)
    coder_id = Column(Integer, ForeignKey('coders.id'))
    coders = relationship(Coders)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }


engine = create_engine('sqlite:///development.db')
Base.metadata.create_all(engine)