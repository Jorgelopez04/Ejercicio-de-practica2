def fahrenheit(f):
  
    celsius=(f-32)*5/9
    
    return celsius


f=float(input("ingrese los grados Fahrenheint: "))
grados=fahrenheit(f)

print(f"la conversion a grados Celsius es {grados}")