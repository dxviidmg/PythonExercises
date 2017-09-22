limite = int(input("Ingrese un numero: "))

suma1=0
suma2=0

for l in range(1, limite+1):
    if l%2==0:
        
        suma1=suma1+l
    else:
        suma2=suma2+l

print("Suma numeros pares", suma1)
print("Suma numeros impares", suma2)
