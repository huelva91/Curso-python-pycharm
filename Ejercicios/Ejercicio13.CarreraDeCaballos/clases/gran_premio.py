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
