l = int(input("Ingrese un limite: "))

for km in range(0, l+1):
    pies = km * 3281
    yardas = round(km * 1093.6, 4)
    millas_n = round(km * 0.5396, 4) 
    millas = round(km * 0.6214, 4)
    print(pies, yardas, millas_n, millas)
