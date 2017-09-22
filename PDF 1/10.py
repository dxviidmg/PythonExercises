limite = int(input("Ingrese el radio: "))

for l in range(1, limite+1):
    for m in range (1, l+1):
        if m**2 == l:
            print(m, "es raiz cuadrada de", l)
    
