class Pago:
    """
    long id
    float valor
    CuentaPorCobrar cXC
    LocalDate fecha
    boolean activa
    """
    def __init__(self):
        pass

    def __init__(self, id, valor, cXC, fecha,activa):
        #un que ya existe
        self.id = int(id)
        self.valor = float(valor)
        self.cXC = cXC
        self.fecha = fecha
        self.activa = activa


    def __int__(self, valor,cXC, fecha):
        #un nuevo
        self.valor = float(valor)
        self.cXC = cXC
        self.fecha = fecha
        self.activa = True

    def __init__(self, datos):
        size = len(datos)
        if(size == 5):
            self.__int__(datos[0],datos[1],datos[2],datos[3])
            pass
        if(size == 3):
            self.__init__(datos[0], datos[1], datos[2])
            pass

