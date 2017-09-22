limite = int(input("Ingrese el limite: "))

for l in range (1, limite+1):
    cont = 0
    for m in range (1, l+1):
        if l%m==0:
            cont = cont + 1
    if cont == 2 or l==1:
        print(l)
            
