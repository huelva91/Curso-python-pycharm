from ..clases.gran_premio import Gran_premio
from ..utils.conexiones import get_mysql_conection
import logging as log

class Gran_premio_DAO:
    _SELECCIONAR = 'SELECT * FROM curso_python.gran_premio ORDER BY id'
    _INSERTAR = 'INSERT INTO `curso_python`.`gran_premio` (`ID`, `NOMBRE`, `DISTANCIA`, `NUM_CARRERAS`) VALUES(%s, ' \
                '%s, %s) '
    _ACTUALIZAR = 'UPDATE `curso_python`.`gran_premio` SET `ID` = %s, `NOMBRE` = %s, `DISTANCIA` = %s, `NUM_CARRERAS` ' \
                  '= %s WHERE (`ID` = %s) '
    _ELIMINAR = 'DELETE FROM `curso_python`.`gran_premio` WHERE ID=%s'

    @classmethod
    def selecionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                gran_premio = []
                for registro in registros:
                    gran_premio = Gran_premio(registro[0], registro[1], registro[2], registro[3])
                    gran_premio.append(gran_premio)

                return gran_premio

    @classmethod
    def insertar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                log.debug("Gran premio insertado:".format(gran_premio))
                return cursor.rowcount

    @classmethod
    def actualizar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras, gran_premio.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug("Gran premio actualizado:".format(gran_premio))
                return cursor.rowcount

    @classmethod
    def eliminar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, gran_premio.id)
                log.debug("Objeto eliminado:".format(gran_premio))


