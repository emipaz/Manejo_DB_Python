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
    cedula_identidad=Column(String)
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
        return'{}{}{}'.format(self.dia,self.hora_inicio, self.hora_fin,\
        self.cedula_identidad)

class Profesor(Base):
    __tablename__='profesor'
    id=Column(Integer, Sequence('profesor_seq_id'),primary_key=True)
    cedula_identidad=Column(String, primary_key=True)    
    nombre_profesor=Column(String)
    apellido_profesor=Column(String)
    
    profe_curso=relationship("Horarios",back_populates='curso_profe')
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
def estaProfesor(Session ses, String identidad, String nombre, String apellido):
     if (identidad == ses.query(Profesor.cedula_identidad).all()):
        print("El profesor ya se encuentra en la base de datos:")
        print(ses.query(Profesor.cedula_identidad.any()).all())
        return True
    elif (nombre == ses.query(Profesor.nombre_profesor.any())&&\
        apellido==ses.query(Profesor.apellido_profesor.any()):
        print("El profesor ya se encuentra en la base de datos:")
        print(ses.query(Profesor.cedula_identidad.any()).all())
        return True
    else:
        return False
    
def estaAlumno(Session ses, String identidad, String nombre, String apellido):
    if (identidad == ses.query(Estudiante.cedula_identidad).all()):
        print("El estudiante ya se encuentra en la base de datos:")
        print(ses.query(Profesor.cedula_identidad.any()).all())
        return True
    elif (nombre == ses.query(Estudiante.nombre_estudiante.any())&&\
        apellido==ses.query(Estudiante.apellido_estudiante.any()):
        print("El estudiante ya se encuentra en la base de datos:")
        print(ses.query(Estudiante.cedula_identidad.any()).all())
        return True
    else:
        return False
    
    
def estaCurso(Session ses, String nom_curso):
    return nom_curso.lower() == ses.query(Curso,Curso.nombre_curso).any().lower()


def agregarProfesor (Session ses):
    identidad= String(input("Ingrese el numero de identidad del profesor:"))
    nombre = String(input("Ingrese Solo el Nombre del Profesor:"))
    apellido = String(input("Ingrese solo el Apellido del Profesor:"))
    if !estaProfesor(ses, identidad, nombre, apellido):
        prof_nuevo = Profesor(nombre_profesor=nombre, apellido_profesor=apellido,\
                              cedula_identidad=identidad)

        ses.add(prof_nuevo)
        ses.commit()
        
            

def agregarCurso(Sessinon ses):
    nombre_cur= String(input("Ingrese el nombre del curso:"))
    if !estaCurso(ses, nombre_cur):
          curso_nuevo = Curso(nombre_curso=nombre_cur)
          
          
          ses.add(curso_nuevo)
          ses.commit()
    else:
          print("El curso {} ya existe".format(nombre_cur))

def agregarAlumno(Sessinon ses):
    identidad= String(input("Ingrese el numero de identidad del estudiante:"))
    nombre = String(input("Ingrese Solo el Nombre del Estudiante:"))
    apellido = String(input("Ingrese solo el Apellido del Estudiante:"))
    if !estaAlumno(ses, identidad, nombre, apellido):
        estud_nuevo = Estudiante(nombre_estudiante=nombre, apellido_estudiante=apellido,\
                              cedula_identidad=identidad)
        ses.add(estud_nuevo)
        ses.commit()

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
#Si ne se quiere eso, comente la linea que llama a esta función en el main y listo
def precargarDatos(Session ses):
###############ESTUDINTES##################################################
    alumno1=Estudiante(nombre_alumno='Raton', apellido_alumno='Perez',
    cedula_identidad='1234567-8')
    alumno2=Estudiante(nombre_alumno='Hugo', apellido_alumno='Donald',\
    cedula_identidad='abcdef123')
    alumno3=Estudiante(nombre_alumno='Paco', apellido_alumno='Donald',\
    cedula_identidad='abcdef124')
    alumno4=Estudiante(nombre_alumno='Luis', apellido_alumno='Donald',\
    cedula_identidad='abcdef125')
    ses.add(alumno1)
    ses.add(alumno2)
    ses.add(alumno3)
    ses.add(alumno4)
############PROFESORES###################################################
    prof1= Profesor(nombre_profesor='Profesor1', apellido_profesor='El 1',\
    cedula_identidad='1234567-9')
    prof2= Profesor(nombre_profesor='Profesor1', apellido_profesor='El 2',\
    cedula_identidad='1234567-10')
    prof1= Profesor(nombre_profesor='Profesor3', apellido_profesor='El 3',\
    cedula_identidad='1234567-11')
    ses.add(prof1)
    ses.add(prof2)
    ses.add(prof3)

#######################Horarios#######################################



#######################Cursos#######################################
    fisica=Curso(nombre_curso="Fisica")
    quimica=Curso(nombre_curso="Quimica")
    biologia=Curso(nombre_curso="Biología")
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