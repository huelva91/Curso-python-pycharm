from Clases import *
import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logs/alumnos.log'),
                    log.StreamHandler()
                ])
lista_colegios = []
with open('alumnos-colegio.txt', 'r', encoding='utf8') as archivo:
    for linea in archivo:
        log.debug(linea)
        lista_datos = linea.rstrip().split("|")
        colegio = Colegio(lista_datos[1], lista_datos[2], lista_datos[3], lista_datos[4])

# print(nombre_colegio)
# nombre_alumno =
