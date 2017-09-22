lista = []
cantidad_elementos = int(input('Cuantidad de elementos: '))

for i in range(cantidad_elementos):
     insertar_numero = int(input('Insertar el numero :'))
     lista.append(insertar_numero)

mayor = 0
menor = 0
suma = 0
producto = 1

for l in lista:
    suma = suma + l
    producto = producto * l
    
    if mayor <= l:
        mayor= l
    else:
        menor = l
        
print("Suma", suma)
print("Promedio", suma/cantidad_elementos)
print("Producto", producto)
print('Mayor: ',mayor)
print('Menor', menor)
