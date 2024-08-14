from models.Proprietario import Proprietario
from repository import RepositoryProprietario as rp

class ServiceProprietario:
    def registrarProprietario(self,datos):
        prop = Proprietario(datos)
        rp.registrarProprietario(datos)
        pass
    def cojerProprietarioId(self, id):
        return rp.cojerProprietarioId(id)
    def cojerProprietarioCedula(self,cedula):
        return rp.cojerProprietarioCedula(cedula)
    def deletar(self,id):
        rp.deletar(id)
    def modificar(self,id,datos):
        update = f"cedula = '{datos[0]}', nombre = '{datos[1]}', direccion = '{datos[2]}'"
        return rp.modificarId(id,update)
        pass