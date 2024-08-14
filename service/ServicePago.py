from models.Pago import Pago
from validation.ValidationPago import ValidationPago
from repository import RepositoryPago as rp
from repository import RepositoryCuentaPorCobrar as cc

class ServicePago():
    def registrarPago(self, datos):
        pg = Pago(datos)
        ValidationPago.validar(pg)
        rp.registrarPago(datos)
        saldo = cc.cojerCuentaPorCobrarId(datos[1]).saldo
        saldo -= datos[0]
        cc.modificar(datos[1], f"saldo = {saldo}")
        pass

    def cojerPagoId(self, id):
        datosPago = rp.cojerPagoId(id)
        return datosPago

    def cojerPagoCliente(self, proprietario):
        return rp.cojerPagoCliente(proprietario)

    def cojerPagoMes(self, periodo):
        return rp.cojerPagoPeriodo(periodo)

    def deletar(self, id):
        cxC = rp.cojerPagoId(id).cXC
        valor = rp.cojerPagoId(id).valor
        cxC.saldo += valor
        rp.deletar(id)
        cc.modificar(cxC.id,f"saldo = {cXC.saldo}")

    def modificar(self, id, datos):
        pg = rp.cojerPagoId(id)
        cxc = cc.cojerCuentaPorCobrarId(pg.cXC.id)
        saldoNovoAntes = cxc.saldo + pg.valor
        cc.modificar(cxc.id,f"saldo = {saldoNovoAntes}")
        update = f"valor = {datos[0]}, cuentaPorCobrar = {datos[1]}, fecha = '{datos[2]}'"
        cxcNova = cc.cojerCuentaPorCobrarId(datos[1])
        saldoNovoAgora = cxcNova.saldo - datos[0]
        cc.modificar(datos[1],f"saldo = {saldoNovoAgora}")
        return rp.modificar(id,update)