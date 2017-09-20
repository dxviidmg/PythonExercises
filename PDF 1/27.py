a = int(input("Ingresa valor de a: "))
b = int(input("Ingresa valor de b: "))
c = int(input("Ingresa valor de c: "))

r = b**2 - 4*a*c
print(r)
if r<0:
    print("La ecuación no tiene solucion")
elif r ==0:
    print("La ecucación tiene una solución")
    print("-b/2a")
else:
    print("La ecuación tiene 2 soluciones")
    print("-b - (√(b²-4 ac))/2")
    print("-b + (√(b²-4 ac))/2")
