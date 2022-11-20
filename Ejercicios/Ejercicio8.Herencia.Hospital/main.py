from hospital import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doctor1 = Doctor(1, "Francisco", "Perez Montes", "Traumatologia")
    doctor2 = Doctor(2, "Maria", "Garcia Garcia", "Traumatologia")
    doctores = [doctor1 , doctor2]

    enfermero1 = Enfermeros("Primera", 3, "Daniel", "Caceres Munoz")
    enfermero2 = Enfermeros("Segunda", 4, "Diana", "Suarez Martin")
    enfermeros = [enfermero1, enfermero1]

    pacientes1 = Pacientes("Tos", 5, "Juan", "Garcia Perez", enfermedades="")
    pacientes2 = Pacientes("Sangrado", 5, "Juan", "Garcia Perez", enfermedades="")
    pacientes = [pacientes1, pacientes2]

    consulta1 = Cosulta(1, doctor1)
    consulta2 = Cosulta(2, doctor2)
    consultas = [consulta1, consulta2]

    habitacion1 = Habitacion(1)
    habitacion2 = Habitacion(2)
    habitacion3 = Habitacion(3)
    habitaciones = [habitacion1, habitacion2, habitacion3]

    doctor1.fichar()
    doctor2.fichar()
