class Persona:
    def __init__(self, id, nombre, apellidos):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos


class Doctor(Persona):
    def __init__(self, especialidad, id, nombre, apellidos):
        Persona.__init__(self, id, nombre, apellidos)
        self.especialidad = especialidad

    def fichar(doctor):
        print("El doctor/a {} acaba de fichar", format(doctor.nombre))


class Enfermeros(Persona):
    def __init__(self, planta, id, nombre, apellidos):
        Persona.__init__(self, id, nombre, apellidos)
        self.planta = planta

    def fichar(self):
        pass


class Pacientes(Persona):
    def __init__(self, sintomas, id, nombre, apellidos):
        Persona.__init__(self, id, nombre, apellidos)
        self.sintomas = sintomas


class Enfermos(Persona):
    def __init__(self, enfermedad, sintomas, id, nombre, apellidos):
        Persona.__init__(self, id, nombre, apellidos)
        Pacientes.__init__(self, sintomas)
        self.enfermedad = enfermedad


class Hospital():
    pass


