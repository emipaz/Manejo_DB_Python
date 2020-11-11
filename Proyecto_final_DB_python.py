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
    cedula_identidad=Column(String, primary_key=True)
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
    cedula_identidad=Column(String, primary_key=True)    
    nombre_profesor=Column(String)
    apellido_profesor=Column(String)
    
    profe_curso=relationship("Horarios",back_populates='curso_profe')
    def __repr__(self):
        return'{}{}'.format(self.nombre_profesor, self.apellido_profesor)


Profesor.__table__
Estudiante.__table__
Curso.__table__
Horarios.__table__
Base.metadata.create_all(engine)
#########################################################################################

##############Definiciones de cada funcion################################
def estaProfesor(Session ses, Profesor prof):
    return prof.cedula_identidad == ses.query(Profesor, Profesor.cedula_identidad).all()
    
def estaAlumno(Session ses, Estudiante estud):
    return estud.cedula_identidad == ses.query(Estudiante, Estudiante.cedula_identidad).all()
    
    
def estaCurso(Session ses, Curso curso):
    return curso.id == ses.query(Curso,Curso.id).all()


def agregarProfesor ():
    #acá tiene que chequear que el profesor no esté en la DB
    print ("Agregar Profesor")

def agregarCurso():
    print("agregar curso")

def agregarAlumno():
    #acá tiene que chequear que el estudiante no esté en la DB
    print ("Agregar Estudiante")

def asignarAlumnoACurso():
#algo aca
    print("Asignar estudiante a curso")

def asignarProfesorACurso():
    print("Asignar profesor a curso")
#algo aca

def asignarHorarioProfCurso():
    return None


def exportarAlumnosPerteneceACurso():
    print ("Exportar alumnos pertenecientes a curso")
#    print(session.query(Curso).filter(Profesor.profe_curso.any()).all())
#    print(session.query(Horarios).filter(Profesor.profe_curso.any()).all())

###############################################################################
#Ésta función es para precargar datos en las DB #
#Si ne se quiere eso, comente las lineas y listo
def precargarDatos(Session ses):
    

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

def ingresar_operacion():
    opcion = 0
    try:
        impr_op_posibles()
        opcion = int(input("Elije una opcion (con numeros)"))

        if opcion < 1 or opcion > 8:
            print("##################################")
            print("ingresa un numero valido por favor")
            print("##################################")
            ingresar_operacion()

    except ValueError:
        print("ingresa un numero valido por favor")
        ingresar_operacion()

    return opcion

def realizar_operacion(operacion, session):
    if (operacion == 8):
        session.close()

    if (operacion ==1):
        agregarAlumno()

    if (operacion ==2):
        agregarProfesor()

    if (operacion ==3):
        AsignarAlumnoACurso()

    if (operacion == 4):
        asignarAlumnoACurso()

    if (operacion == 5):
        asignarProfesorACurso()

    if (operacion == 6):
        asignarHorarioProfCurso()

    if (operacion == 7):
        exportarAlumnosPerteneceACurso(session)

 

#############Main#############################################################
def main():
    Session = sessionmaker(bind=engine)
    session = Session()

    operacion = 0
    precargarDatos(session)
    while operacion != 8:
        operacion = ingresar_operacion()
        realizar_operacion(operacion, session)

    print ("Gracias por usar nuestro sistema de escuela")

if __name__ == '__main__':
    main()