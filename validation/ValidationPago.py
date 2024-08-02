from Validation import Validation

class ValidationPago(Validation):
    def validar(self, obj):
        if(obj.valor > obj.cXC.valor):
            raise Exception("Valor pago mayor que valor cobrado")
        if(obj.valor<=0):
            raise Exception("Tiene que pagar algo")