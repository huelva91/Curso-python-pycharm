from Ejercicios.Ejercicio13CarreraDeCaballos.clases import *
from clases_dao import *

def leer_ficheros():
    datos = []

    with open("ficheros/caballos.txt", 'r', encoding='utf8') as archivo:
        for index, line in enumerate(archivo):
            lista = line.split("|")
            new_caballo = Caballos(index + 1, lista[0], lista[1], int(lista[2]), int(lista[3]), int(lista[4]),
                                 int(lista[5]))
            caballos.append(new_caballo)

    with open("ficheros/apostantes.txt", 'r',
              encoding='utf8') as archivo:
        for index, line in enumerate(archivo):
            lista = line.split("|")
            new_apostante = Apostantes(index+1, lista[0], int(lista[1]))
            apostantes.append(new_apostante)

    with open("ficheros/grandes_premios.txt", 'r',
              encoding='utf8') as archivo:
        for index, line in enumerate(archivo):
            lista = line.split("|")
            new_Granpremio = Gran_premio(index + 1, lista[0], int(lista[1]), int(lista[2]))
            gran_premio.append(gran_premio)





caballos = []
apostantes = []
gran_premio = []