class retirar:
    def __init__(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron ${cantidad} de la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")