from modelo.cuenta import CuentaBancaria
from modelo.depositar import depositar
cuenta1= CuentaBancaria(numero_cuenta=1040,propietarios="Juan",balance=500)



print(f"su cuenta es {cuenta1.numero_cuenta} el propietario es {cuenta1.propietarios} y su balance es {cuenta1.balance}")



