from models.PropriedadHorizontal import PropriedadHorizontal
from validation.ValidationPropriedadHorizontal import ValidationPropriedadHorizontal
from repository import RepositoryLogin as rl

class ServiceLogin:
    def registarPH(self,datos):
        pH = PropriedadHorizontal(datos)
        ValidationPropriedadHorizontal(pH)
        rl.registarPH(datos)
        pass
    def login(self,nome,senha):
        return rl.login(nome,senha)
    def modificar(self,datos,id):
        pH = PropriedadHorizontal(datos)
        ValidationPropriedadHorizontal(pH)
        update = f"nombre = '{datos[0]}', direccion = '{datos[1]}', senha = '{datos[2]}'"
        rl.modificar(update,id)
        pass