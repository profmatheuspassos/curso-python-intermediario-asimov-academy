# A vantagem do raise é que o código já para na hora - não dando sequência, economizam-se recursos

import math

def calcularRaizQuadrada(numero):
    if numero < 0:
        raise ValueError(f"Impossível calcular raiz quadrada de número negativo.")
    return math.sqrt(numero)

for n in [4, 2, 1, 0, -1]:
    print(f"A raiz quadrada de {n} é igual a {calcularRaizQuadrada(n)}.")