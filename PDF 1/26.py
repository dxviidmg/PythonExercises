a = int(input("Ingresa valor de a: "))
b = int(input("Ingresa valor de b: "))
c = int(input("Ingresa valor de c: "))

if a>0 and b>0 and c>0:
    if a == b and a == c:
        print("Equilatero")
    elif a == b or a == c or b==c:
        print("Isoceles")
    else:
        print("Escaleno")
else:
    print("No se aceptan ceros o números negativos")
