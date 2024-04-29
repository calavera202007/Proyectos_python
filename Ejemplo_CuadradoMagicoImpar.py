import numpy as np

def magico(matriz):
    f = len(matriz)
    c = len(matriz[0])
    conta = 1
    j = c // 2
    i = 0;
    while conta <= f*c:
        matriz[i][j] = conta
        if conta % f == 0:
            i = i + 1
        else:
            if j == f - 1:
                j = 0
            else:
                j = j + 1
            if i == 0:
                i = f - 1
            else:
                i = i - 1
        conta = conta + 1
    #print(matriz)
    return matriz

filas =  int(input("Numero de Filas y columnas: "))
columnas = filas
if filas % 2 == 1:
    A=np.zeros([filas,columnas])
    mat = magico(A)
    print (mat)
    
else:
    print("N no es impar no se puede generar el Cubo mágico:")

