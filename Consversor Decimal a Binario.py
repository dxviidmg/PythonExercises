numero = int(input("Escribe un numero decimal: "))
binario = ''

while True:
    print(numero)
    if numero % 2 == 0:
        binario = '0' + binario
    else:
        binario = '1' + binario
        
    numero = numero // 2
    if numero == 0:
        break;
                
print(binario)
