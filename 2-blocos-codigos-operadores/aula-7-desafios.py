# Desafio 01
# Crie uma função que retorna se um número inteiro n (maior que zero) é primo.
print("Crie uma função que retorna se um número inteiro n (maior que zero) é primo.")

def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = 10
if numero > 0:
    if primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
else:
    print("Número tem de ser maior que zero.")

for i in [1, 5, 10, 13, 15, 17]:
    print(f"O número {i} é número primo? --> {primo(i)}")

print("\n")

# Desafio 2
# Transformar funções usando operadores e expressões para simplificar o código abaixo

import random
import time

print("Transformar funções usando operadores e expressões para simplificar o código abaixo - ver funções no arquivo")

print("\nResolução com código original")

def busca_dados():
    if random.random() > 0.5:
        return None
    return 'xxxxx'

def processa_dados(dados):
    return f'Dados "{dados}" foram processados'

dados_banco = busca_dados()

if dados_banco is not None:
    dados_processados = processa_dados(dados_banco)
else:
    dados_processados = 'N/A'

print(f'Resultado: {dados_processados}')

print("\nResolução com código alterado")

def busca_dados2():
    return None  if (random.random() > 0.5) else 'xxxxx'

def processa_dados2(dados2):
    return f'Dados "{dados2}" foram processados'

dados_processados2 = (dados_processados2 := processa_dados2(busca_dados2())) if (busca_dados2() is not None) else 'N/A' # Solução minha

dados_processados2 = (processa_dados2(dados_buscados)) if (dados_buscados := busca_dados2() is not None) else 'N/A' # Sugestão do professor

print(f'Resultado: {dados_processados2}')

# Desafio 3
# 