limite = int(input("Ingrese un numero: "))
for i in range (2 , limite+1):
    
    sumaDivisores = 0
    for j in range (1, i+1):
        if i%j==0 and i!=j:
            sumaDivisores = sumaDivisores + j
    if i == sumaDivisores:
        print(i, "es un numero perfecto")
    elif i > sumaDivisores:
        print(i, "es un numero deficiente")
    else:
        print(i, "es un numero abundante")
        
        
    
