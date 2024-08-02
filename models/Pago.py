class Pago:
    """
    long id
    float valor
    CuentaPorCobrar cXC
    LocalDate fecha
    """
    def __init__(self):
        pass

    def __init__(self, id, valor, cXC, fecha):
        self.id = int(id)
        self.valor = float(valor)
        self.cXC = cXC
        self.fecha = fecha

    def __init__(self, datosCompletos):
        self.__int__(datosCompletos[0],datosCompletos[1],datosCompletos[2],datosCompletos[3])

    def __int__(self, valor,cXC, fecha):
        self.valor = float(valor)
        self.cXC = cXC
        self.fecha = fecha

    def __init__(self,datosCreacion):
        self.__init__(datosCreacion[0],datosCreacion[1],datosCreacion[2])
