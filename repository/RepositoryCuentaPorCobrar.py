from CreationDataBase import CreationDataBase
from models.CuentaPorCobrar import CuentaPorCobrar
from models.CuentaPorCobrarExtra import CuentaPorCobrarExtra
from RepositoryProprietario import cojerProprietarioId

dataBase = CreationDataBase()
table = "CuentaPorCobrar"


def registrarCuentaPorCobrar(datos):
    dataBase.insert(table,"valor, propriedadHorizontal,devedor,detalle,periodo,saldo,activa,is_extra",
                    f"{datos[0]},{datos[1]},{datos[2]},'{datos[3]}','{datos[4]}',{datos[5]},1,{datos[6]}")
    pass

def cojerCuentaPorCobrarIdyPh(id, pH):
    datosCuenta = dataBase.select("*",table,f"WHERE Id={id} AND propriedadHorizontal = {pH} AND activa = 1")
    propriedad = cojerProprietarioId(datosCuenta[3])
    datosCuenta[3] = propriedad
    if(datosCuenta[7] == 1):
        return CuentaPorCobrarExtra(datosCuenta)
    return CuentaPorCobrar(datosCuenta)

def cojerCuentasPorCobrarCliente(cliente, pH):
    datosCuentas = dataBase.select("*",table,f"WHERE devedor = {cliente} AND propriedadHorizontal = {pH} AND saldo != 0"
                                             f"activa = 1")
    cuentas = map(conveter,datosCuentas)
    return cuentas

def cojerCuentasPorCobrarMes(periodo):
    datosCuentas = dataBase.select("*",table,f"WHERE activa = 1 AND saldo != 0 AND periodo = '{periodo}'")
    cuenta = map(conveter,datosCuentas)
    return cuenta

def deletar(id):
    dataBase.deleteDesactiva(table,id)
    pass

def modificar(id, update):
    dataBase.update(table, update, f"Id={id}")
    return cojerCuentaPorCobrarId(id)

def cojerCuentaPorCobrarId(id):
    datosCuenta = dataBase.select("*",table,f"WHERE Id = {id}")
    propriedad = cojerProprietarioId(datosCuenta[3])
    datosCuenta[3] = propriedad
    if (datosCuenta[7] == 1):
        return CuentaPorCobrarExtra(datosCuenta)
    return CuentaPorCobrar(datosCuenta)


def moficarValorTodas(porcentaje,periodo, pH):

    cojerCuentasPorCobrarMes()
    pass

def conveter(datosCuenta):
    if(datosCuenta[7] == 1):
        return CuentaPorCobrarExtra(datosCuenta)
    return CuentaPorCobrar(datosCuenta)