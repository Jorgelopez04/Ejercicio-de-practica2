from modelo.cuenta import CuentaBancaria
from modelo.depositar import depositar
from modelo.retirar import retirar
from modelo.detalles import detalles
from modelo.cuota import cuota



mi_cuenta = CuentaBancaria("1040", ["Juan Alvarez"], 1000)


mi_cuenta.depositar(500)
mi_cuenta.retirar(400)
mi_cuenta.cuota()


mi_cuenta.detalles()



