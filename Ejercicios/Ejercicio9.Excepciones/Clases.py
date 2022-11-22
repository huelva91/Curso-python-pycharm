import random
from abc import ABC
import Excepciones as ex
import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logs/Bar_Cafe.log'),
                    log.StreamHandler()
                ])


class Taza_cafe:
    def __init__(self, temperatura, tipo):
        self.temperatura = temperatura
        self.tipo = tipo


class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre


class Cliente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tomar_taza_cafe(self, taza_cafe):

        if taza_cafe.temperatura > 70:
            log.info("El cliente {} ha comentado que esta muy caliente".format(self.nombre))
            raise ex.TooHotTemperatureException("Cafe muy caliente")
        elif taza_cafe.temperatura < 20:
            log.info("El cliente {} ha comentado que esta frio".format(self.nombre))
            raise ex.TooColdTemperatureException("Cafe muy frio")


class Camarero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def servir_taza_cafe(self):
        tipos_de_cafe_lista = ["Cortado", "Manchado", "Americano", "Solo largo"]
        temperatura_aleatoria = random.randint(0, 100)
        tipo_de_cafe = random.choice(tipos_de_cafe_lista)
        taza_cafe = Taza_cafe(temperatura_aleatoria, tipo_de_cafe)
        log.info("El camarero {} ha servido una taza de {} a {} grados".format(self.nombre, tipo_de_cafe,
                                                                               temperatura_aleatoria))
        return taza_cafe


class Bar:
    def __init__(self, camarero):
        self.camarero = camarero

    def atender_cliente(self, cliente):
        taza_cafe = camarero.servir_taza_cafe()
        try:
            cliente.tomar_taza_cafe(taza_cafe)
        except ex.TooHotTemperatureException as thte:
            log.error(thte.message)
        except ex.TooColdTemperatureException as tcte:
            log.error(tcte.message)
        except Exception as e:
            log.error("Al cliente le pasa algo")
        else:
            log.info(
                "El cliente {} se ha tomado un buen cafe a {} grados".format(cliente.nombre, taza_cafe.temperatura))


if __name__ == '__main__':
    cliente = Cliente("Cliente 1")
    camarero = Camarero("Camarero 1")
    bar = Bar(camarero)
    bar.atender_cliente(cliente)
