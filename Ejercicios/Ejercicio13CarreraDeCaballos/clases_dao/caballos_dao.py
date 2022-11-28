from Ejercicios.Ejercicio13CarreraDeCaballos.clases import Caballos
from Ejercicios.Ejercicio13CarreraDeCaballos.utils.conexiones import get_mysql_conection
import logging as log


class Caballos_DAO:
    _SELECCIONAR = 'SELECT * FROM curso_python.caballos ORDER BY id'
    _INSERTAR = 'INSERT INTO `curso_python`.`caballos` (`ID`, `NOMBRE`, `FECHA_NACIMIENTO`, `VELOCIDAD`, `EXPERIENCIA`, `VALOR_APUESTA` ) VALUES(%s, ' \
                '%s, %s, %s, %s, %s) '
    _ACTUALIZAR = 'UPDATE `curso_python`.`caballos` SET `ID` = %s, `NOMBRE` = %s, `FECHA_NACIMIENTO` = %s, `VELOCIDAD` = %s, `EXPERIENCIA` = %s, `VALOR_APUESTA` = %s, WHERE (`ID` = %s) '
    _ELIMINAR = 'DELETE FROM `curso_python`.`caballos` WHERE id=%s'

    @classmethod
    def selecionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                caballos = []
                for registro in registros:
                    caballos = Caballos(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5] )
                    caballos.append(caballos)

                return caballos

    @classmethod
    def insertar(cls, caballos):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballos.nombre, caballos.fecha_nacimiento, caballos.velocidad, caballos.experiencia, caballos.valor_apuesta)
                cursor.execute(cls._INSERTAR, valores)
                log.debug("Gran premio insertado:".format(caballos))
                return cursor.rowcount

    @classmethod
    def actualizar(cls, caballos):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballos.nombre, caballos.fecha_nacimiento, caballos.velocidad, caballos.experiencia, caballos.valor_apuesta)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug("Gran premio actualizado:".format(caballos))
                return cursor.rowcount

    @classmethod
    def eliminar(cls, caballos):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, caballos.id)
                log.debug("Objeto eliminado:".format(caballos))

