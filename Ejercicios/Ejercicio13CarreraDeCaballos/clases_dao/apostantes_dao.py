from Ejercicios.Ejercicio13CarreraDeCaballos.clases import Apostantes
from Ejercicios.Ejercicio13CarreraDeCaballos.utils.conexiones import get_mysql_conection
import logging as log

class Apostantes_DAO:
    _SELECCIONAR = 'SELECT * FROM curso_python.apostantes ORDER BY id'
    _INSERTAR = 'INSERT INTO `curso_python`.`apostantes` (`ID`, `NOMBRE`, `SALDO`) VALUES(%s, ' \
                '%s, %s) '
    _ACTUALIZAR = 'UPDATE `curso_python`.`apostantes` SET `ID` = %s, `NOMBRE` = %s, `SALDO` = %s,  WHERE (`ID` = %s) '
    _ELIMINAR = 'DELETE FROM `curso_python`.`apostantes` WHERE ID=%s'

    @classmethod
    def selecionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                apostantes = []
                for registro in registros:
                    apostantes = Apostantes(registro[0], registro[1], registro[2])
                    apostantes.append(apostantes)

                return apostantes

    @classmethod
    def insertar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostantes.id, apostantes.nombre, apostantes.saldo)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug("Gran premio insertado:".format(apostantes))
                return cursor.rowcount

    @classmethod
    def actualizar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostantes.nombre, apostantes.saldo, apostantes.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug("Gran premio actualizado:".format(apostantes))
                return cursor.rowcount

    @classmethod
    def eliminar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, apostantes.id)
                conexion.commit()
                log.debug("Objeto eliminado:".format(apostantes))

apostante1 = Apostantes(1, "juan", 300)
apostanteDao = Apostantes_DAO.insertar(apostante1)