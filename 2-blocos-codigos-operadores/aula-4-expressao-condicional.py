# Expressões condicionais - forma resumida de escrever um if-else
print("Expressões condicionais - forma resumida de escrever um if-else")
x = 4
y = 5
maiorValor = x if x > y else y
print("x = 5, y = 4")
print("maiorValor = x if x > y else y")
print(f"Maior valor: {maiorValor}")

print("\n")

# Uso comum em funções que retornam valores simples
def pegarCor(valor):
    return "vermelho" if valor < 0 else "azul"

for valor in [-1, 0, 1]:
    print(f"A cor do valor {valor} é {pegarCor(valor)}")

print("\n")

# Números pares elevados ao quadrado com compreensão de listas e expressão condicional
print("Números pares elevados ao quadrado com compreensão de listas e expressão condicional")
print("numeros = [1, 2, 3, 4]")
print("paresQuadrados = [n ** 2 if n % 2 else n for n in numeros]")
numeros = [1, 2, 3, 4]
paresQuadrados = [
    n ** 2
    if n % 2
    else n
    for n in numeros
]
print(f"Números normais: {numeros}")
print(f"Pares ao quadrado: {paresQuadrados}")