import random

op = random.randint(1, 4)

# Usando if
if op == 1:
    print("Opção 1")
elif op == 2:
    print("Opção 2")
else:
    print("Opção inválida")

# Usando match case
match op:
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case _:
        print("Opção inválida")

# Usando match case em um dicionário
notas = {
    "João": 10,
    "Maria": 9,
    "José": 8
}
match notas:
    case {"João": 9}:
        print("João tirou nota 10!")
    case _:
        print("Nenhuma informação encontrada...")

# Usando match case em um dicionário apenas na chave
notas = {
    "João": 10,
    "Maria": 9,
    "José": 8
}
match notas:
    case {"João": _}:
        print("João está no dicionário!")
    case _:
        print("Nenhuma informação encontrada...")