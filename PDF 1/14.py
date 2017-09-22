print("Grados centigrados a grados Fahrenheit: 1")
print("Grados Fahrenheit a grados centigrados: 2")
seleccion = int(input("Seleccione conversión: "))

if seleccion == 1:
    c = int(input("Centigrados: "))
    f = 9/5*c + 32
    print(f, "°F")
elif seleccion == 2:
    f = int(input("Centigrados: "))
    c = (f-32)*5/9
    print(c, "°C")
else:
    print("Error en la selección")
