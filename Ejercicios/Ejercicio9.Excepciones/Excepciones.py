class TemperaturaException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje


class TooHotTemperatureException(TemperaturaException):

    def __init__(self, mensaje):
        TemperaturaException.__init__(self, mensaje=mensaje)


class TooColdTemperatureException(TemperaturaException):

    def __init__(self, mensaje):
        TemperaturaException.__init__(self, mensaje=mensaje)
