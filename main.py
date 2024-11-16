import math
# import matplotlib.pyplot as plt

for j in range(3150): 
    sequence = [len(j)]

for i in range(len(sequence)):
    sequence[i] = i + 1 - i + 2
    print("Objeto atual: ", sequence[i])
