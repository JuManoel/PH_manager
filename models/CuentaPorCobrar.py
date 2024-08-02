class CuentaPorCobrar:
    """
    long id
    float valor
    PropriedadHorizontal pH
    Proprietario devedor
    int mes
    string detalle
    """
    def __init__(self):
        pass

    def __init__(self, id, valor, pH, devedor,mes, detalle):
        self.id = int(id)
        self.valor = float(valor)
        self.pH = pH
        self.devedor = devedor
        self.mes = int(mes)
        self.detalle = str(detalle)

    def __init__(self, datosCompletos):
        self.__int__(datosCompletos[0], datosCompletos[1], datosCompletos[2], datosCompletos[3],datosCompletos[4],
                     datosCompletos[5])

    def __int__(self, valor, pH, devedor,mes,detalle):
        self.valor = float(valor)
        self.pH = pH
        self.devedor = devedor
        self.mes = int(mes)
        self.detalle = str(detalle)

    def __init__(self, datosCreacion):
        self.__init__(datosCreacion[0], datosCreacion[1], datosCreacion[2],datosCreacion[3],datosCreacion[4])