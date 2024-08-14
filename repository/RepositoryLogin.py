from CreationDataBase import CreationDataBase
from models.PropriedadHorizontal import PropriedadHorizontal

dataBase = CreationDataBase()
table = "PropriedadHorizontal"

def registarPH(datos):
    dataBase.insert(table,"nombre,senha,direccion",f"'{datos[0]}','{datos[1]}','{datos[2]}'")

def login(nome, senha):
    datosUser = dataBase.select("Id,senha",table,f"WHERE nombre = '{nome}'")
    if(datosUser[1] != senha):
        assert False, "Senha incorrecta"
    return datosUser[1]

def modificar(update,id):
    dataBase.update(table,update,f"Id = {id}")