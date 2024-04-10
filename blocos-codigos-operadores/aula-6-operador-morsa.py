# Operador morsa: ":="
print("Operador morsa: \":=\n")
print("Ver explicação no conteúdo do arquivo.\n")

"""
ESTRUTURA ORIGINAL
valorBusca = "xxx"

resultado = buscarBancoDados(valorBusca)
if resultado is None:
    print(f"Nada foi encontrado para o valor de busca {valorBusca}.")
else:
    print(f"Resultados encontrados para valor de busca {valorBusca}: {resultado}")

ESTRUTURA COM MORSA
valorBusca = "xxx"

if (resultado := buscarBancoDados(valorBusca)) is None:
    print(f"Nada foi encontrado para o valor de busca {valorBusca}.")
else:
    print(f"Resultados encontrados para valor de busca {valorBusca}: {resultado}")
"""
print("Sem morsa")
n = 5
while n > 0:
    n -= 1
    print(n)
print("\n")
print("Com morsa")
n = 5
while (n := n - 1) >= 0:
    print(n)