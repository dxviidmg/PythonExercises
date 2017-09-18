def Sumatoria(n):
    if n==1:
        return 1
    else:   
        s = n + Sumatoria(n-1)
        return s

print(Sumatoria(4))
