from Validation import Validation

class ValidationCuentaPorCobrar(Validation):
    def validar(self, obj):
        if(obj.valor<=0):
            raise Exception("Tienes que cobrar Algo")
        if(obj.mes<=0 or obj.mes>12):
            raise Exception("Periodo Invalido")