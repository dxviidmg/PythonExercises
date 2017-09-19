a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
cociente = 0

while a > b:
    cociente = cociente + 1
    a = a - b

    residuo = a - (b * cociente)

print("Cociente: ", cociente)
print("Residuo", a )    
