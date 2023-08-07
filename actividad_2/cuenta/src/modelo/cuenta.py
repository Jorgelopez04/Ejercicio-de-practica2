




class CuentaBancaria:

    def __init__(self,numero_cuenta,propietarios,balance):
        self.numero_cuenta=numero_cuenta
        self.propietarios= propietarios
        self.balance=balance


    def depositar(self, monto,balance):
        self.monto=monto
        self.balance=monto+balance
       

    def retirar(self, monto,balance):
        self.monto=monto
        self.balance=monto-balance


    def cuota(self,balance):
        self.cuota_manejo =balance*0.02
        self.balance=self.balance-self.cuota_manejo

 


    
      

cuenta1= CuentaBancaria(numero_cuenta=1040,propietarios="Juan",balance=500)
print(f"su cuenta es {cuenta1.numero_cuenta} el propietario es {cuenta1.propietarios} y su balance es {cuenta1.balance}")



cuenta1.depositar(monto= 1000,balance=500)
print("Nuevo balance:", cuenta1.balance)

cuenta1.retirar(monto=1000,balance=500)
print("el retiro que has realizado es de",cuenta1.balance)

cuenta1.cuota(balance=500)
print("su cuota de manejo es de ",cuenta1.balance)