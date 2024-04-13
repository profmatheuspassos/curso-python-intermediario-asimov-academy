# Argumentos arbitrários com *args e **kwargs

def somar(*valores):
    return sum(valores)

print(somar(1, 2, 3, 4))

print("\n")

def somar2(*valores, **valores2): # Aqui com um * são passados os parâmetros sem nome, e com dois ** são passados os parâmetros com nomes
    return sum(valores)

print(somar2(1, 2, 3, 4, x = 5, y = 6))

print("\n")

def exibeArgs(*args, **kwargs):
    print("exibeArgs")
    print(f"Argumentos passados sem palavras-chave: {args}")
    print(f"Argumentos passados com palavras-chave: {kwargs}")

exibeArgs(1, 2, 3, 4, x = 5, y = 6)

print("\n")

def exibeArgs2(a, b, *args, **kwargs):
    print("exibeArgs2")
    print(a, b)
    print(f"Argumentos passados sem palavras-chave: {args}")
    print(f"Argumentos passados com palavras-chave: {kwargs}")

exibeArgs2(1, 2, 3, 4, x = 5, y = 6)

print("\n")

def exibeArgs3(*args, **kwargs):
    print(f"Argumentos passados sem palavra-chave: {args}")
    print(f"Argumentos passados com palavra-chave: {kwargs}")

valores = [1, 2, 3]
dic = {
    "nome": "Juliano",
    "idade": 30
}
print("Passa lista e dicionário sem desmembrá-los")
exibeArgs3(valores, dicionario = dic) # Passa lista e dicionário sem desmembrá-los
print("Passa lista e dicionário com desmembramento")
exibeArgs3(*valores, **dic) # Passa lista e dicionário com desmembramento