
class depositar:

   def __Init__(self, cantidad):
        self.balance += cantidad
        print(f"Se depositaron ${cantidad} en la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}") 