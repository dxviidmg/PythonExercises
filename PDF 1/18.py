lim = int(input("Ingrese el valor de limite: "))
x = int(input("Ingrese el valor de x  "))

factorial = 1
e = 1
for l in range (1, lim+1):
    div = x**l
    factorial = factorial * l
    r = div/factorial
    e = e + r

print(e)


    

    
