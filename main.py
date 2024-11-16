import math

GetNdoc = int(input("Ndoc: "))

def calculate(ndoc): # isso só existe pelo return
    sequence = []
    formula = 0

    for i in range(ndoc):
        sequence += [i] # formula = i + 1 - i + 2
        for k in range(len(sequence)):
            print("Objeto atual: ", sequence[k])

calculate(GetNdoc)