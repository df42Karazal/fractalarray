import math
from functools import lru_cache
# import turtle

GetNdoc = int(input("Numero do concurso: "))
# GetData = [int(input("Dia: ")), int(input("Mês: ")), int(input("Ano: "))]
# tur = turtle.Turtle()

""" for k in range(len(GetData)):
    GetData[k] = GetData[k] + 1  """
@lru_cache(100)
def fib(N):
    if N <= 1:
        return 1
    return fib(N - 1) + fib(N - 2)

sequence = [fib(i) for i in range(GetNdoc)]
print("Objetos: ", sequence)