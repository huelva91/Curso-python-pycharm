from hospital import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    doctor1 = Doctor(1, "Francisco", "Perez Montes", "Traumatologia")
    doctor2 = Doctor(2, "Maria", "Garcia Garcia", "Traumatologia")


    enfermero1 = Enfermeros("Primera", 3, "Daniel", "Caceres Munoz")
    enfermero2 = Enfermeros("Segunda", 4, "Diana", "Suarez Martin")

    pacientes1 = Pacientes("Tos", 5, "Juan", "Garcia Perez", enfermedades="")
    pacientes2 = Pacientes("Sangrado", 5, "Juan", "Garcia Perez", enfermedades="")