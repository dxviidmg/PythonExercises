promedio = float(input("Promedio: "))

print("\n")
print("A: Sonara, Chihuahua, Baja California Norte, Nuevo León")
print("B: San Luis Potosí, Edo. México, D.F., Puebla")
print("C: Oaxaca, Chiapas, Campeche")
print("D: Estados que no se encuentran en los acuerdos con el D.F")
zona = input("Zona: ")

print("\n")
print("1: Publica")
print("2: Privada")
tipo_escuela = input("Tipo de escuela: ")

if promedio >=0 and promedio <=10:
    if zona == "A" or zona == "B" or zona == "C" or zona == "D":
        if tipo_escuela == "1" and tipo_escuela == 2:
            
        else:
            print("error tipo escuelas")
    else:
        print("Error en zonas")
else:
    print("Numero fuera de rango de 0 a 10")
