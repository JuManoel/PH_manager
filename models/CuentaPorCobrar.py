class CuentaPorCobrar:
    """
    long id
    float valor
    PropriedadHorizontal pH
    Proprietario devedor
    int mes
    string detalle
    float saldo
    boolean activa
    """
    def __init__(self):
        pass

    def __init__(self, id, valor, pH, devedor,periodo, detalle, saldo,activa):
        #para cojer una cuenta que ya existe
        self.id = int(id)
        self.valor = float(valor)
        self.pH = pH
        self.devedor = devedor
        self.periodo = int(periodo)
        self.detalle = str(detalle)
        self.saldo = float(saldo)
        self. activa = activa



    def __int__(self, valor, pH, devedor,periodo,detalle):
        #Para crear una nueva cuenta de cobro
        self.valor = float(valor)
        self.pH = pH
        self.devedor = devedor
        self.periodo = int(periodo)
        self.detalle = str(detalle)
        self.saldo = self.valor
        self. activa = True

    def __init__(self, datos):
        size = len(datos)
        if(size == 5):
            self.__init__(datos[0], datos[1], datos[2],datos[3],datos[4])
            pass
        if(size == 8):
            self.__int__(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
            pass

