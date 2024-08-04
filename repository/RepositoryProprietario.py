from CreationDataBase import CreationDataBase
from models.Proprietario import Proprietario

dataBase = CreationDataBase()
table = "Proprietario"
is_activa = "AND activa = 1"

def registrarProprietario(datos):
    dataBase.insert(table,"cedula, nombre, direccion, propriedadHorizontal,activa",
                    f"'{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}',1")

def cojerProprietarioId(id):
    datosPro = dataBase.select("*",table,f"Id={id} {is_activa}")
    prop = Proprietario(datosPro)

def cojerProprietarioCedula(cedula):
    datosPro = dataBase.select("*", table, f"cedula={cedula} {is_activa}")
    prop = Proprietario(datosPro)
    pass

def deletar(id):
    dataBase.deleteDesactiva(table,id)
    pass

def modificarId(id, update):
    dataBase.update(table, update, f"Id={id}")
    pass