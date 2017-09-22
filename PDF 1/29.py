promedio = float(input("Promedio: "))

print("\n")
print("1: Publica")
print("2: Privada")
tipo_escuela = input("Tipo de escuela: ")

print("\n")
print("A: Sonara, Chihuahua, Baja California Norte, Nuevo León")
print("B: San Luis Potosí, Edo. México, D.F., Puebla")
print("C: Oaxaca, Chiapas, Campeche")
print("D: Estados que no se encuentran en los acuerdos con el D.F")
zona = input("Zona: ")

#Validación de promedio
if promedio >=0 and promedio <=10:
    #Validación de zonas
    if zona == "A" or zona == "B" or zona == "C" or zona == "D":
        #Validación de tipo de escuela
        if tipo_escuela == "1" or tipo_escuela == "2":
            #Opciones de escuelas publicas en zonas A. B, C
            if tipo_escuela == "1" and (zona == "A" or zona == "B" or zona == "C"):
                if promedio >= 9.5:
                    print("Ayuda economica: $3000")
                elif (promedio < 9.5 and promedio >= 8) and (zona == "A" or zona == "B"):
                    print("Ayuda economica: $2200")
                elif (promedio < 9.5 and promedio >= 8) and zona == "C":
                    print("Ayuda economica: $1900")
                elif (promedio < 8 and promedio >= 7) and (zona == "A" or zona == "C"):
                    print("Ayuda economica: $1500")
                elif (promedio < 8 and promedio >= 7) and zona == "B":
                    print("Ayuda economica: $1200")
                elif promedio < 7 and zona == "B":
                    print("Ayuda economica: $500")
                else:
                    print("Cuota fija: $1000")
            #Opciones de escuelas privadas en zonas A. B, C
            elif tipo_escuela == "2" and (zona == "A" or zona == "B" or zona == "C"):
                ant_beca = input("¿Ha estado Becado antes?: Si tu respuesta es Si, oprime 1: ")
                if ant_beca == "1":
                    print("Ayuda economica: $500")
                else:
                    print("Cuota fija: $1000")

            #Opciones de escuelas en zona D o promedio menor a 7
            elif zona == "D" or promedio < 7:
                #Escuelas publicas
                if tipo_escuela == "1":
                    print("Cuota fija: $1000")
                #Escuelas privadas
                else:
                    print("Cuota fija: $2000")
        else:
            print("Error, al ingresar el tipo de escuela")
    else:
        print("Error, al ingresar zona")
else:
    print("Error, numero fuera de rango de 0 a 10")
