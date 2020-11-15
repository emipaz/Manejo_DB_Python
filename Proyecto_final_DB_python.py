#Sistema de escuelas por Jenifer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

###############Creación de la base de datos #########################################
engine  = create_engine('sqlite:///:memory:')
Base    = declarative_base(engine)

class Estudiante(Base):
    __tablename__    = "alumno"
    id               = Column(Integer,Sequence('alumno_seq_id'),primary_key=True)
    cedula_identidad = Column(String)
    nombre_alumno    = Column(String)
    apellido_alumno  = Column(String)
    curso_idAlumno   = Column(Integer,ForeignKey('curso.id'))
    cursos           = relationship("Curso",back_populates='estudiantes')
    def __repr__(self):
        return'{}{}'.format(self.nombre_alumno, self.apellido_alumno)

class Curso(Base):
    __tablename__='curso'
    id           = Column(Integer, Sequence('curso_seq_id'),primary_key=True)
    nombre_curso = Column(String)
    estudiantes  = relationship("Estudiante",back_populates='cursos')
    hora_curso   = relationship("Horarios",back_populates='curso_hora')
    def __repr__(self):
        return'{}'.format(self.nombre_curso)

class Horarios(Base):
    __tablename__='horario'
    id           =  Column(Integer, Sequence('horario_seq_id'),primary_key=True)
    dia          = Column(String)
    hora_inicio  = Column(String)
    hora_fin     = Column(String)
    profesor_id  = Column(Integer,ForeignKey('profesor.id'))
    curso_id     = Column(Integer,ForeignKey('curso.id'))
    curso_hora   = relationship("Curso",back_populates='hora_curso')
    curso_profe  = relationship("Profesor",back_populates='profe_curso')

    def __repr__(self):
        return'{}{}{}'.format(self.dia,self.hora_inicio, self.hora_fin,\
        self.cedula_identidad)

class Profesor(Base):
    __tablename__     = 'profesor'
    id                = Column(Integer, Sequence('profesor_seq_id'), primary_key = True)
    cedula_identidad  = Column(String) #.primary_key = True)    
    nombre_profesor   = Column(String)
    apellido_profesor = Column(String)
    profe_curso       = relationship("Horarios",back_populates='curso_profe')
    def __repr__(self):
        return'{}{}{}'.format(self.nombre_profesor, self.apellido_profesor,\
        self.cedula_identidad)


Profesor.__table__
Estudiante.__table__
Curso.__table__
Horarios.__table__
Base.metadata.create_all(engine)
#########################################################################################

##############Definiciones de cada funcion################################
def estaProfesor(ses, identidad, nombre, apellido):
    if ses.query(Profesor).filter(Profesor.cedula_identidad == identidad):
        print("El estudiante ya se encuentra en la base de datos:")
        return True

    elif ses.query(Profesor).filter(Profesor.nombre_profesor == nombre) and ses.query(Profesor).filter(Profesor.apellido_profesor == apellido):

        print("El estudiante ya se encuentra en la base de datos:")
        print ( ses.query(Estudiante).Estudiante(cedula_identidad.any()).all())
        return True
    else:
        return False
    
def estaAlumno(ses, identidad, nombre, apellido):
    #print(ses, identidad, nombre, apellido)
    if ses.query(Estudiante).filter(Estudiante.cedula_identidad == identidad):
        print("El estudiante ya se encuentra en la base de datos:")
        return True
    elif ses.query(Estudiante).filter(Estudiante.nombre_alumno == nombre) and ses.query(Estudiante).filter(Estudiante.apellido_alumno == apellido):
        print("El estudiante ya se encuentra en la base de datos:")
        print(ses.query(Estudiante).Estudiante(cedula_identidad.any()).all())
        return True
    else:
        return False
    
    
def estaCurso(ses, nom_curso):
    print(ses.query( Curso ).filter ( Curso.nombre_curso == nom_curso ))

    query = ses.query( Curso ).filter ( Curso.nombre_curso == nom_curso ).all()
    
    print("hola soy el querry",query)
    print("hola soy el curso",nom_curso.lower())

    for i in query:
        print(i,type(i))
        print( nom_curso.lower(),type(nom_curso))
        print("es este",nom_curso.lower() == i)
        a = (nom_curso.lower())

        if nom_curso.lower() == str(i):
            break
    else:
        print(False)
        return False
    print(True)
    return True
    
    #return nom_curso.lower() == query


def agregarProfesor (ses):
    identidad  = String(input("Ingrese el numero de identidad del profesor:"))
    nombre     = String(input("Ingrese Solo el Nombre del Profesor:"))
    apellido   = String(input("Ingrese solo el Apellido del Profesor:"))
    if estaProfesor(ses, identidad, nombre, apellido):
        prof_nuevo = Profesor(nombre_profesor   = nombre, 
                              apellido_profesor = apellido,\
                              cedula_identidad  = identidad)

        ses.add(prof_nuevo)
        ses.commit()


def agregarCurso(ses):
    nombre_cur = input("Ingrese el nombre del curso:")
    print(nombre_cur,type(nombre_cur))
    if not estaCurso(ses, nombre_cur):
          curso_nuevo = Curso(nombre_curso = nombre_cur)
          #acá hace falta agregar los horarios
          ses.add(curso_nuevo)
          ses.commit()
    else:
          print("El curso {} ya existe".format(nombre_cur))

def agregarAlumno(ses):
    identidad = input("Ingrese el numero de identidad del estudiante:")
    print(identidad)
    nombre    = input("Ingrese Solo el Nombre del Estudiante:")
    apellido  = input("Ingrese solo el Apellido del Estudiante:")
    print(estaAlumno(ses, identidad, nombre, apellido))
    if estaAlumno(ses, identidad, nombre, apellido):
        estud_nuevo = Estudiante(nombre_alumno       = nombre,
                                 apellido_alumno     = apellido,
                                 cedula_identidad    = identidad)
        ses.add(estud_nuevo)
        ses.commit()

def asignarAlumnoACurso(ses):
    
    print("Asignar estudiante a curso")

def asignarProfesorACurso():
    print("Asignar profesor a curso")
#algo aca

def asignarHorarioProfCurso():
    return None


def exportarAlumnosPerteneceACurso(ses):
    for curso in session.query(Curso).filter(Profesor.profe_curso.any()).all():
        print("Nombre del curso:" + curso)
    print(session.query(Horarios).filter(Profesor.profe_curso.any()).all())



###############################################################################
#Ésta función es para precargar datos en las DB #
#Si ne se quiere eso, comente la linea que llama a esta función en el main y listo
def precargarDatos(ses):
###############ESTUDINTES##################################################
    alumno1 = Estudiante(nombre_alumno    = 'Raton', 
                         apellido_alumno  = 'Perez',
                         cedula_identidad = '1234567-8')
    alumno2 = Estudiante(nombre_alumno    = 'Hugo', 
                         apellido_alumno  = 'Donald',\
                         cedula_identidad = 'abcdef123')
    alumno3 = Estudiante(nombre_alumno    = 'Paco', 
                         apellido_alumno  = 'Donald',\
                         cedula_identidad = 'abcdef124')
    alumno4 = Estudiante(nombre_alumno    = 'Luis', 
                         apellido_alumno  = 'Donald',\
                        cedula_identidad  = 'abcdef125')
    ses.add(alumno1)
    ses.add(alumno2)
    ses.add(alumno3)
    ses.add(alumno4)
############PROFESORES###################################################
    prof1 = Profesor(nombre_profesor   = 'Profesor1', 
                     apellido_profesor = 'El 1',
                     cedula_identidad  = '1234567-9')
    prof2 = Profesor(nombre_profesor   = 'Profesor1', 
                     apellido_profesor = 'El 2',
                     cedula_identidad  = '1234567-10')
    prof3 = Profesor(nombre_profesor   = 'Profesor3', 
                     apellido_profesor = 'El 3',\
                     cedula_identidad  = '1234567-11')
    ses.add(prof1)
    ses.add(prof2)
    ses.add(prof3)

#######################Horarios#######################################



#######################Cursos#######################################
    fisica   = Curso( nombre_curso = "Fisica")
    quimica  = Curso( nombre_curso = "Quimica")
    biologia = Curso( nombre_curso = "Biología")
    ses.add(fisica)
    ses.add(quimica)
    ses.add(biologia)
    
    ses.commit()
####################################################################################################


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
        print("##################################")
        print("ingresa un numero valido por favor")
        print("##################################")
        ingresar_operacion()

    return opcion

def realizar_operacion(operacion, session):
    if (operacion == 8):
        session.close()

    if (operacion ==1):
        agregarAlumno(session)

    if (operacion ==2):
        agregarCurso(session)

    if (operacion ==3):
        AsignarAlumnoACurso(session)

    if (operacion == 4):
        asignarAlumnoACurso(session)

    if (operacion == 5):
        asignarProfesorACurso(session)

    if (operacion == 6):
        asignarHorarioProfCurso(session)

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