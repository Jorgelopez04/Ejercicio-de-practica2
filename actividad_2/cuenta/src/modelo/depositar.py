from modelo.cuenta import CuentaBancaria
class depositar:

    def __init__(self, monto):
        self.monto=monto
        monto.cuentabancaria.append(self)
        print("monto agregado")