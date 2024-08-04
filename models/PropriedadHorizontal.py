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


    def __init__(self,nombre,direccion,senha):
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.senha = str(senha)

    def __init__(self, datos):
        size = len(datos)
        if(size == 4):
            self.__int__(datos[0],datos[1],datos[2],datos[3])
            pass
        if(size == 3):
            self.__init__(datos[0], datos[1], datos[2])
            pass



