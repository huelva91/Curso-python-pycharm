class TemperaturaException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje


class TooHotTemperatureException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje


class TooColdTemperatureException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje
