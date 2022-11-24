class Alumno:
    def __init__(self, nombre_colegio, nombre_alumno, apellidos_alumno, dni_alumnos, asignaturas):
        self._nombre_alumno = nombre_alumno
        self._apellidos_alumno = apellidos_alumno
        self._dni_alumnos = dni_alumnos
        self._asignaturas = asignaturas

        # Atributo  nombre colegio


    # Atributo  nombre_alumno
    @property
    def nombre_alumno(self):
        return self._nombre_alumno

    @nombre_alumno.setter
    def nombre_alumno(self, nombre_alumno):
        self._nombre_alumno = nombre_alumno

    # Atributo  apellidos_alumno
    @property
    def apellidos_alumno(self):
        return self._apellidos_alumno

    @apellidos_alumno.setter
    def apellidos_alumno(self, apellidos_alumno):
        self._apellidos_alumno = apellidos_alumno

    # Atributo  dni_alumnos
    @property
    def dni_alumnos(self):
        return self._nombre_alumno

    @dni_alumnos.setter
    def dni_alumnos(self, dni_alumnos):
        self._dni_alumnos = dni_alumnos

    # Atributo  asignaturas
    @property
    def asignaturas(self):
        return self._asignaturas

    @asignaturas.setter
    def asignaturas(self, asignaturas):
        self._asignaturas = asignaturas

class Colegio:
    def __init__(self, nombre_colegio):
        self._nombre_colegio = nombre_colegio

    @property
    def nombre_colegio(self):
        return self._nombre_colegio

    @nombre_colegio.setter
    def nombre(self, nombre_colegio):
        self._nombre_colegio = nombre_colegio
