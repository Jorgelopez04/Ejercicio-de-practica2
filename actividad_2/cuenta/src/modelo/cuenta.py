



class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se depositaron ${cantidad} en la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")
    
    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron ${cantidad} de la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")
        else:
            print("Fondos insuficientes para retirar.")
    
    def cuota(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2% (${cuota}) en la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")
    
    def detalles(self):
        print(f"Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: ${self.balance}")


