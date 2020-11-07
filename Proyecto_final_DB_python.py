#Sistema de escuelas por Jenifer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

###############Creación de la base de datos #########################################
engine=create_engine('sqlite:///:memory:')
Base=declarative_base(engine)

class Estudiante(Base):
    __tablename__="alumno"   
    id=Column(Integer,Sequence('alumno_seq_id'),primary_key=True)
    nombre_alumno=Column(String)
    apellido_alumno=Column(String)
    curso_ida=Column(Integer,ForeignKey('curso.id'))
    
    cursos=relationship("Curso",back_populates='estudiantes')
    def __repr__(self):
        return'{}{}'.format(self.nombre_alumno, self.apellido_alumno)

class Curso(Base):
    __tablename__='curso'
    id=Column(Integer, Sequence('curso_seq_id'),primary_key=True)
    nombre_curso=Column(String)
        
    estudiantes=relationship("Estudiante",back_populates='cursos')
    hora_curso=relationship("Horarios",back_populates='curso_hora')
    def __repr__(self):
        return'{}'.format(self.nombre_curso)

class Horarios(Base):
    __tablename__='horario'
    id=Column(Integer, Sequence('horario_seq_id'),primary_key=True)
    dia=Column(String)
    hora_inicio=Column(String)
    hora_fin=Column(String)
    profesor_id=Column(Integer,ForeignKey('profesor.id'))
    curso_id=Column(Integer,ForeignKey('curso.id'))
    
    curso_hora=relationship("Curso",back_populates='hora_curso')
    curso_profe=relationship("Profesor",back_populates='profe_curso')

    def __repr__(self):
        return'{}{}{}'.format(self.dia,self.hora_inicio, self.hora_fin)

class Profesor(Base):
    __tablename__='profesor'
    id=Column(Integer, Sequence('profesor_seq_id'),primary_key=True)
    nombre_profesor=Column(String)
    apellido_profesor=Column(String)
    
    profe_curso=relationship("Horarios",back_populates='curso_profe')
    def __repr__(self):
        return'{}{}'.format(self.nombre_profesor, self.apellido_profesor)


Base.metadata.create_all(engine)
#########################################################################################

##############Definiciones de cada funcion################################
def AgregarProfesor ():



def AgregarAlumno(Session sesion, Estudiante alumno):
    if sesion:
        #algo acá
        session.commit()




def ExportarAlumnosPerteneceACurso():
    print(session.query(Curso).filter(Profesor.profe_curso.any()).all())
    print(session.query(Horarios).filter(Profesor.profe_curso.any()).all())
    #acá va un query
###############################################################################



Session=sessionmaker(bind=engine)
session=Session()



print(horario1.curso_profe)


