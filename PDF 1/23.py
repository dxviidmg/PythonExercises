altura = int(input("Ingrese un numero: "))
if altura > 0 and altura <= 10:
    if altura == 1:
        print("**")
    elif altura == 2:
        print(" **")
        print("++++")
    else:
        print(" "*(altura-1) + "**")
        for i in range (1 , altura-1):
            if i %2==0:
                print(" "*(altura-i-1) + "*" + (str(i)*i)*2 + "*")
            else:
                print(" "*(altura-i-1) + "+" + (str(i)*i)*2 + "+")
            
        if altura %2 == 0:
            print("+"*altura*2)
        else:
            print("*"*altura*2)
else:
    print("Rango no aceptado")

