binario = input("Escribe un numero binario: ")
cont = 0
decimal = 0

for digito in binario:
    longitud = len(binario)    
    cont = cont + 1
    potencia = longitud - cont
    multiplo = 2**potencia
    num = multiplo * int(digito)
    decimal = decimal + num

print(decimal)

    

    
