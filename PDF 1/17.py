limite = int(input("Ingrese el limite fraccionario de pi"))

cont=0

pi=0
for l in range (1, limite+1, 2):

    frac = 4/l
    
    cont=cont+1
    if cont%2==1:
        pi=pi+frac
    else:
        pi=pi-frac

    print(pi)

print(pi)

    
