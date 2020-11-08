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
    curso_idAlumno=Column(Integer,ForeignKey('curso.id'))
    
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
def estaProfesor():
def estaAlumno():
def estaCurso():


def agregarProfesor (Session sesion, Profesor profe):
    #acá tiene que chequear que el profesor no esté en la DB




def agregarAlumno(Session sesion, Estudiante alumno):
    #acá tiene que chequear que el profesor no esté en la DB

def asignarAlumnoACurso():
#algo aca

def asignarProfesorACurso():
#algo aca

def asignarProfesorACurso():
#algo aca

def asignarHorarioProfCurso():



def exportarAlumnosPerteneceACurso(Session session):
    print(session.query(Curso).filter(Profesor.profe_curso.any()).all())
    print(session.query(Horarios).filter(Profesor.profe_curso.any()).all())

###############################################################################

#############Funcion que despliega el menú##########################################################
def impr_op_posibles():
  print("Estas son las operaciones  que se pueden hacer")
  print("1 - agregar alumno")
  print("2 - agregar curso")
  print("3 - agregar profesor")
  print("4 - asignar un alumno a un curso")
  print("5 - asignar un profesor a un curso")
  print("6 - asignar un horario a un profesor de un curso")
  print("7 - listar para cada curso, los alumnos y los profesores con sus horarios")
  print("8 - salir")
  
print("Bienvenidos al sistema de escuela")


#############Main#############################################################
Session=sessionmaker(bind=engine)
session=Session()
continuar = "si"
while (continuar == "si") :
  impr_op_posibles() #imprime el menú

###############Acá pide y chequea que lo que le estás dando es un numero#############################
  try:
    operacion= float(input("Introduce el numero de operacion que quieres realizar: "))
  except ValueError:
    print("no se reconoce esa operacion")
    continue #Si lo que el usuario ingresa no es un número, imprime que no se reconoce la operacion y va al while
  else:
    if (operacion == 8):
        continuar = "no"
        session.close()
    else:
        if (operacion ==1):
            agegarCurso()
            continue
        if (operacion ==2):
            agregarProfesor()
            continue
        if (operacion ==3):
            AsignarAlumnoACurso()
            continue
        if (operacion == 4):
            asignarAlumnoACurso()
            continue
        if (operacion == 5):
            asignarProfesorACurso()
            continue
        if (operacion == 6):
            asignarHorarioProfCurso()
            continue
        if (operacion == 7):
            exportarAlumnosPerteneceACurso(session):
            continue
###########Esto es para saber si desea continuar en el sistema#############################
    while (continuar != "si") and (continuar != "no"):
        continuar = input("La operacion ingresada no es valida. Desea continuar(SI/no): ")
        continuar = continuar.lower()
        if (continuar == "no"):
            session.close()
print ("Gracias por usar nuestro sistema de escuela")
exit()