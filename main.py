import math

GetNdoc = int(input("Numero do concurso: "))
global r

def dectobin(x):
    return int(bin(x)[2:])

def formula():
    array = []
    for i in range(15):
        array += [i]
    r = array.count(1)
    tmp = r
    soma = 0
    [array for k in str(r)]
    for j in range(0, len(array)):
        soma = soma + array[j];
        print("Resultado: ", soma)
dectobin(GetNdoc)
formula()
