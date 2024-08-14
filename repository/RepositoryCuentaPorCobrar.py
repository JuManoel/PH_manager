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
    datosCuentas = dataBase.select("*",table,f"WHERE devedor = {cliente} AND propriedadHorizontal = {pH}"
                                             f" AND saldo != 0 AND activa = 1")
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
    dataBase.update(table, update, f"Id={id} AND activa = 1")
    return cojerCuentaPorCobrarId(id)

def cojerCuentaPorCobrarId(id):
    datosCuenta = dataBase.select("*",table,f"WHERE Id = {id} AND activa = 1")
    propriedad = cojerProprietarioId(datosCuenta[3])
    datosCuenta[3] = propriedad
    if (datosCuenta[7] == 1):
        return CuentaPorCobrarExtra(datosCuenta)
    return CuentaPorCobrar(datosCuenta)


def moficarValorTodas(porcentaje,periodo, pH):
    ultimoPeriodo = dataBase.select("periodo",table,"ORDER BY periodo DESC LIMIT 1 WHERE activa = 1")[0]
    mes = int(ultimoPeriodo.split("-")[1])
    mes = mes + 1 if mes+1<=12 else 1
    ano = int(ultimoPeriodo.split("-")[0])
    ano = ano if mes!=1 else ano+1
    novoPeriodo = f"{ano}-{mes}"
    datosUltimoPeriodo = dataBase.select("valor, propriedadHorizontal,devedor,detalle,periodo,saldo,activa,is_extra",
                                         table,
                                         f"WHERE propriedadHorizontal = {pH} AND periodo = {ultimoPeriodo}"
                                         f" AND is_extra = 0 AND ACTIVA = 1")
    for i in datosUltimoPeriodo:
        dataBase.insert(table,"valor, propriedadHorizontal,devedor,detalle,periodo,saldo,activa,is_extra",
                        f"{i[0]*(1+(porcentaje/100))},{i[1]},{i[2]},'{i[3]}','{novoPeriodo}',1,0")
    pass

def conveter(datosCuenta):
    if(datosCuenta[7] == 1):
        return CuentaPorCobrarExtra(datosCuenta)
    return CuentaPorCobrar(datosCuenta)