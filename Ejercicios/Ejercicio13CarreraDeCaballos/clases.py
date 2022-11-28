class Gran_premio:
    def __init__(self, id, nombre, distancia, num_carreras):
        self._id = id
        self._nombre = nombre
        self._distancia = distancia
        self._num_carreras = num_carreras

    # Atributo  id_gran_premio
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # Atributo  nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Atributo  distancia
    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, distancia):
        self._distancia = distancia

    # Atributo  num_carreras
    @property
    def num_carreras(self):
        return self._num_carreras

    @num_carreras.setter
    def num_carreras(self, num_carreras):
        self._num_carreras = num_carreras


class Caballos:
    def __init__(self, id, nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        # self._id_granpremio = id_granpremio

    # Atributo  id_caballos
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # Atributo  nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Atributo  fecha_nacimiento
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

        # Atributo  velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    # Atributo  experiencia
    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    # Atributo  valor_apuesta
    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self, valor_apuesta):
        self._valor_apuesta = valor_apuesta

    # Atributo  id_granpremio
    # @property
    # def id_granpremio(self):
    #     return self._id_granpremio
    #
    # @id_granpremio.setter
    # def id_granpremio(self, id_granpremio):
    #     self._id_granpremio = id_granpremio


class Apostantes:
    def __init__(self, id, nombre, saldo):
        self._id = id
        self._nombre = nombre
        self._saldo = saldo

    # Atributo  id_apostante
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # Atributo  nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Atributo  saldo
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
