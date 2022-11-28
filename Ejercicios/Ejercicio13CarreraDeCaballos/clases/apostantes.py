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
