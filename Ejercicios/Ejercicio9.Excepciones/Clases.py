import random
import Excepciones as ex
import logging as log


class Taza_cafe:
    def __init__(self, temperature, tipo):
        self.temperature = temperature
        self.tipo = tipo


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Cliente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tomar_taza_cafe(self, taza_cafe):
        try:
            if taza_cafe.temperatura > 70:
                log.warning("El cliente {} ha comentado que esta muy caliente".format(self.nombre))
                raise ex.TooHotTemperatureException("Cafe muy caliente")
            else:
                log.warning("El cliente {} ha comentado que esta frio".format(self.nombre))
                raise ex.TooColdTemperatureException("Cafe muy frio")
        except:
            pass


class Camarero(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def servir_taza_cafe(self):
        tipos_de_cafe_lista = ["Cortado", "Manchado", "Americano", "Solo largo"]
        temperatura_aleatoria = random.randint(0, 100)
        tipo_de_cafe = random.choice(tipos_de_cafe_lista)
        taza1 = Taza_cafe(temperatura_aleatoria, tipo_de_cafe)
        log.info("El camarero {} ha servido una taza de {} a {} grados".format(self.nombre, tipo_de_cafe,
                                                                               temperatura_aleatoria))


class Bar:
    pass


camarero1 = Camarero("Juan")
camarero1.servir_taza_cafe()
