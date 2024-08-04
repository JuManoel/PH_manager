class Proprietario:
    """
    @AutoIncremente
    long id
    @Unique
    string cedula
    string nombre
    string direccion
    PropriedadHorizontal pH
    boolean activa
    """
    def __init__(self):
        pass

    def __init__(self, id,cedula, nombre, direccion, pH, activa):
        self.id = int(id)
        self.cedula = str(cedula)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.pH = pH
        self.activa = activa


    def __int__(self, cedula, nombre, direccion, pH):
        self.cedula = str(cedula)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.pH = pH
        self.activa = True

    def __init__(self, datos):
        size = len(datos)
        if(size == 6):
            self.__int__(datos[0],datos[1],datos[2],datos[3], datos[4], datos[5])
            pass
        if(size == 4):
            self.__init__(datos[0], datos[1], datos[2], datos[3])
            pass
