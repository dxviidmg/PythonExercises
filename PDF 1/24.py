segundos = int(input("Ingrese un una cantidad en segundos: "))
if len(str(segundos)) <=5 and (segundos)>0:
    horas = 0
    minutos = 0
    
    while segundos > 3600:
        horas = horas + 1
        segundos = segundos - 3600
    while segundos > 60:
        minutos = minutos + 1
        segundos = segundos - 60

    print("Horas:", horas, ". Minutos: ", minutos, ". Segundos: ", segundos, ".")

    
else:
    print("Numero fuera de rango: Mayor de 5 digitos o es negativo")
