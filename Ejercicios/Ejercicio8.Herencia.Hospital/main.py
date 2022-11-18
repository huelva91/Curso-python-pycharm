import hospital

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    doctor1 = hospital.Doctor("Traumatologia", 1, "Francisco", "Perez Montes")
    doctor1 = hospital.Doctor("Traumatologia", 2, "Maria", "Garcia Garcia")

    enfermero1 = hospital.Enfermeros("Primera", 3, "Daniel", "Caceres Munoz")
    enfermero2 = hospital.Enfermeros("Segunda", 4, "Diana", "Suarez Martin")

    pacientes1 = hospital.Pacientes("Tos", 5, "Juan", "Garcia Perez")
    pacientes2 = hospital.Pacientes("Sangrado", 5, "Juan", "Garcia Perez")