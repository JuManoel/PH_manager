class Proprietario:
    """
    @AutoIncremente
    long id
    @Unique
    string cedula
    string nombre
    string direccion
    PropriedadHorizontal pH
    """
    def __init__(self):
        pass

    def __init__(self, id,cedula, nombre, direccion, pH):
        self.id = int(id)
        self.cedula = str(cedula)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.pH = pH

    def __init__(self, datosCompletos):
        self.__int__(datosCompletos[0],datosCompletos[1],datosCompletos[2],datosCompletos[3], datosCompletos[4])

    def __int__(self, cedula, nombre, direccion, pH):
        self.cedula = str(cedula)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.pH = pH

    def __init__(self, datosCreacion):
        self.__init__(datosCreacion[0], datosCreacion[1], datosCreacion[2], datosCreacion[4])