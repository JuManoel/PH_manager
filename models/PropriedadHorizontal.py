class PropriedadHorizontal:
    """
    @AutoIncremente
    long id
    @Unique
    String nombre
    string direccion
    @Rule(5 character, 1 number, 1 special character)
    string senha
    """
    def __init__(self):
        pass
    def __int__(self, id,nombre, direccion, senha):
        self.id = int(id)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.senha = str(senha)

    def __init__(self, datosCompletos):
        self.__int__(datosCompletos[0],datosCompletos[1],datosCompletos[2],datosCompletos[3])

    def __init__(self,nombre,direccion,senha):
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.senha = str(senha)

    def __init__(self,datosCreacion):
        self.__init__(datosCreacion[0],datosCreacion[1],datosCreacion[2])


