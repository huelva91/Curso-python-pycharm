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

    def tomar_taza_cafe(self):
        pass


class Camarero(Persona):
    def __init__(self, nombre):
        self.nombre = nombre

    def servir_taza_cafe(self):
        pass


class Bar:
    pass
