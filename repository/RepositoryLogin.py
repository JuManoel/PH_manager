from CreationDataBase import CreationDataBase
from models.PropriedadHorizontal import PropriedadHorizontal

dataBase = CreationDataBase()
table = "PropriedadHorizontal"

def registarPH(datos):
    dataBase.insert(table,"nombre,senha,direccion",f"'{datos[0]}','{datos[1]}','{datos[2]}'")

def login(nome, senha):
    datosUser = dataBase.select("Id,nombre,direccion,senha",table,f"WHERE nombre = '{nome}'")
    if(datosUser[3] != senha):
        assert False, "Senha incorrecta"
    user = PropriedadHorizontal(datosUser)
    return Id

def modificar(update,id):
    dataBase.update(table,update,f"Id = {id}")