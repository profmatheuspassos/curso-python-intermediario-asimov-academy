print("Maneira simples de usar o try-except")

try: # Tenta fazer o que está neste bloco
    x = float(input("Digite um número: "))
    y = float(input("Digite um divisor: "))
    resultado = x / y
except: # É executado se der erro no bloco try
    print("ERRO")
else: # É executado se der tudo certo com o bloco try
    print(resultado)
finally: # É executado não importa o que aconteça - com ou sem erro. Pode ser ignorado, colocando-se o código abaixo fora da indentação
    print("Final do código")

print("\n")

print("Maneira complexa de usar o try-except")

try:
    x = float(input("Digite um número: "))
except ValueError:
    x = 10
    print(f"Valor inválido para x. Continuando o programa com valor padrão de x = {x}")
try:
    y = float(input("Digite um divisor: "))
except ValueError:
    y = 2
    print(f"Valor inválido para y. Continuando o programa com valor padrão de x = {x}")
try:
    resultado = x / y
except ZeroDivisionError:
    print(f"Não é possível dividir um número por zero")
else:
    print(f"O resultado da divisão é {resultado}")