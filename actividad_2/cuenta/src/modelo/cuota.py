class cuota:
    def __init__(self):
     cuota = self.balance * 0.02
     self.balance -= cuota
     print(f"Se aplicó una cuota de manejo del 2% (${cuota}) en la cuenta {self.numero_cuenta}. Nuevo balance: ${self.balance}")