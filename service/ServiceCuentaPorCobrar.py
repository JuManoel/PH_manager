from models.CuentaPorCobrar import CuentaPorCobrar
from models.CuentaPorCobrarExtra import CuentaPorCobrarExtra
from validation.ValidationCuentaPorCobrar import ValidationCuentaPorCobrar

class ServiceCuentaPorCobrar():
    def __init__(self,tipo_Cuenta):
        self.tipo_Cuenta = tipo_Cuenta
    def registrarCuentaPorCobrar(self,datos):
        pass
    def cojerCuentaPorCobrarId(self, id):
        pass
    def cojerCuentasPorCobrarCliente(self,cliente):
        pass
    def cojerCuentasPorCobrarMes(self,mes):
        pass
    def deletar(self,id):
        pass
    def modificar(self,id,datos):
        pass
    def moficarValorTodas(self,porcentaje):
        pass