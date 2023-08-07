from modelo.cuenta import CuentaBancaria
from modelo.depositar import depositar


numero_cuenta = "1234567890"
propietarios = ["Juan Pérez", "María Gómez"]
balance = 5000.0

cuenta1 = CuentaBancaria(numero_cuenta, propietarios, balance)


depositar(cuenta1, 1000)  


print("Nuevo balance:", cuenta1.balance)




