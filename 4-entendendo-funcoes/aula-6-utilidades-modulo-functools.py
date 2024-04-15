import functools

print("Versão sem functools.cache")

def fatorial(n):
    print(f"Valor de n: {n}")
    if n == 1:
        return n
    return n * fatorial(n - 1)

print(fatorial(4))
print(fatorial(4))

print("\n")

print("Versão com functools.cache")

@functools.cache
def fatorial(n):
    print(f"Valor de n: {n}")
    if n == 1:
        return n
    return n * fatorial(n - 1)

print(fatorial(4))

print(fatorial(4))

print("\n")

print("functools.partial")

def somar(a, b):
    return a + b

somarDois = functools.partial(somar, 2)

print(somarDois(3))

# A functools.partial é interessante quando houver argumentos fixos e só seja interessante alterar um dos valores da função

ordenarPorTamanho = functools.partial(
    sorted,
    key = lambda x: len(x) if isinstance(x, str) else x
)

lista = ["abc", 1, 4, 6.5, ".", "22"]

print(ordenarPorTamanho(lista))