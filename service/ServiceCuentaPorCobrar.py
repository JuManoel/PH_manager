from models.CuentaPorCobrar import CuentaPorCobrar
from models.CuentaPorCobrarExtra import CuentaPorCobrarExtra
from validation.ValidationCuentaPorCobrar import ValidationCuentaPorCobrar
from repository import RepositoryCuentaPorCobrar as rc

class ServiceCuentaPorCobrar():
    def __init__(self,tipo_Cuenta):
        self.tipo_Cuenta = tipo_Cuenta
    def registrarCuentaPorCobrar(self,datos):
        cuenta = self.tipo_Cuenta(datos)
        ValidationCuentaPorCobrar(cuenta)
        rc.registrarCuentaPorCobrar(datos)
        pass
    def cojerCuentaPorCobrarId(self, id):
        return rc.cojerCuentaPorCobrarId(id)
        pass
    def cojerCuentasPorCobrarCliente(self,cliente, pH):
        return rc.cojerCuentasPorCobrarCliente(cliente, pH)
        pass
    def cojerCuentasPorCobrarMes(self,periodo):
        return rc.cojerCuentasPorCobrarMes(periodo)
        pass
    def deletar(self,id):
        rc.deletar(id)
        pass
    def modificar(self,id,datos):
        cuentaOriginal = rc.cojerCuentaPorCobrarId(id)
        valorO = cuentaOriginal.valor
        saldoO = cuentaOriginal.saldo
        pago = valor - saldo
        cuenta = self.tipo_Cuenta(datos)
        ValidationCuentaPorCobrar(cuente)
        update = f"valor = {datos[0]},devedor = {datos[1]}, detalle = {datos[2]}, periodo = {datos[3]}, saldo = {datos[0]- pago}"
        pass
    def moficarValorTodas(self,porcentaje):
        pass