import random

class Hospital():
    def __init__(self, doctores, enfermeros, salas_espera, consultas, habitaciones):
        self.doctor = doctores
        self.enfermeros = enfermeros
        self.pacientes = []
        self.enfermos = []
        self.sala_esper = salas_espera
        self.consultas = consultas
        self.habitaciones = habitaciones



class Sala_espera:
    def __int__(self, id, espacios_disponibles):
        self.id = id
        self.espacios_disponibles = espacios_disponibles
        self.paciente = []


class Cosulta:
    def __init__(self, id, doctor):
        self.id = id
        self.doctor = doctor
        self.pacientes = []

class Habitacion:
    def __init__(self, id, ocupada = False):
        self.id = id
        self.ocupada = ocupada
        self.enfermo = None


class Persona:
    def __init__(self, id, nombre, apellidos):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos


class Doctor(Persona):
    def __init__(self, id, nombre, apellidos, especialidad):
        Persona.__init__(self, id, nombre, apellidos)
        self.especialidad = especialidad

    def fichar(self):
        print("El doctor/a {} acaba de fichar".format(self.nombre))

    def diagnosticar_paciente(self, doctor, paciente):
        enfermedades = ["Viruela", "Ebola", "Sarampion"]
        numero_aleatorio_gravedad = random.randint(1, 10)

        if numero_aleatorio_gravedad > 7:
            enfermo = Enfermos(paciente.id, paciente.nombre, paciente.apellidos, enfermedades[0])
            return enfermo
        else:
            "El paciente se ecuentra bien y se va a casa"
            return None


class Enfermeros(Persona):
    def __init__(self, id, nombre, apellidos, planta):
        Persona.__init__(self, id, nombre, apellidos)
        self.planta = planta

    def fichar(self):
        print("El enfermero/a {} acaba de fichar".format(self.nombre))


class Pacientes(Persona):
    def __init__(self, id, nombre, apellidos, sintomas, enfermedades):
        Persona.__init__(self, id, nombre, apellidos)
        self.sintomas = sintomas
        self.enfermedades = enfermedades


class Enfermos(Persona):
    def __init__(self, id, nombre, apellidos, enfermedad):
        Persona.__init__(self, id, nombre, apellidos)
        self.enfermedad = enfermedad
        self.habitacion = None
