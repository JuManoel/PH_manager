from CreationDataBase import CreationDataBase
from RepositoryCuentaPorCobrar import cojerCuentaPorCobrarId
from models.Pago import Pago

dataBase = CreationDataBase()
table = "Pago"

def registrarPago(datos):
    dataBase.insert(table,"valor,cuentaPorCobrar,fecha,activa",
                    f"{datos[0]},{datos[1]},'{datos[2]}',1")
    pass

def cojerPagoId(id):
    datosPago = dataBase.select("*",table,f"WHERE Id = {id}")
    return converterDatos(datosPago)

def cojerPagoCliente(proprietario):
    datosPagos = dataBase.select("*",table+" p","JOIN CuentaPorCobrar cc ON p.cuentaPorCobrar = cc.Id"
                                           " JOIN Proprietario pes ON cc.devedor = pes.Id "
                                           f"WHERE pes.id = :{proprietario};")
    return map(converterDatos,datosPagos)

def cojerPagoMes(periodo):
    datosPago = dataBase.select("*",table,f"WHERE fecha = %{periodo}")
    return map(converterDatos,datosPago)
    pass

def deletar(id):
    dataBase.deleteDesactiva(table,id)
    pass

def modificar(id, update):
    dataBase.update(table, update, f"Id={id}")
    return cojerPagoId(id)

def converterDatos(datosPago):
    cuentaPorCobrar = cojerCuentaPorCobrarId(datosPago[2])
    datosPago[2] = cuentaPorCobrar
    return Pago(datosPago)