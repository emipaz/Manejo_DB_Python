from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class Alumnos(Base):
    id=

class Profesores(Base):

horarios = Table(Base.metadata,
            Column())
class Horarios(Base):
    
    def __repr__(self):
        return "{} {}".format(self.dias, self.horas)
 
class Cursos(Base):
    __tablename__='cursos'

    curso_id = Column(Integer, primary_key = True)
    nombre_curso = Column(String)
    dias,horas = relationship("Book", back_populates ="horarios", cascade="all, delete, delete-orphan"
   