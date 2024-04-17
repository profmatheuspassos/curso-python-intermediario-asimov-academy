import locale # Permite que se converta algo para alguma língua específica - por exemplo, vírgula como separador de valor decimal
import re # Expressões regulares

print("Usando locale")
locale.setlocale(locale.LC_ALL, "")
print(locale.setlocale(locale.LC_ALL, ""))
x = 12.5
print(locale.str(x))
y = 1279.95402
print(locale.currency(y, grouping = True))

print("\n")

print("Usando REGEX")
padrao = "[0-9]"
texto = "Escrevi este texto há 8 anos."
encontra = re.search(padrao, texto)
print(encontra)
print(encontra.group)
print(encontra.start(), encontra.end())
texto2 = "Escrevi este texto há oito anos."
encontra2 = re.search(padrao, texto2)
print(encontra2)

texto = "O ônibus saiu com 45min de atraso, Estava previsto para sair 16h30"
padrao = '[0-9]{2}' # Exatamente 2 dígitos seguidos
match = re.search(padrao, texto)
print(match) # output: <re.Match object; span=(18, 20), match='45'>
print(re.findall(padrao, texto)) # Output: uma lista com os números 45, 16, 30
padrao = '[0-9]{2}h' # Match anterior seguido de caratere 'h'
match = re.search(padrao, texto)
print(match) # output: <re.Match object; span=(61, 64), match='16h'>
padrao = '[0-9]{2}$' # Exatamente 2 dígitos no final da frase
match = re.search(padrao, texto)
print(match) # output: <re.Match object; span=(64, 66), match='30'>
padrao = 'E.' # Caractere "E" seguido de qualquer caractere
match = re.search(padrao, texto)
print(match) # output: <re.Match object; span=(35, 37), match='Es'>
padrao = 'E.*' # Caractere "E" seguido de quaisquer caracteres (plural!)
match = re.search(padrao, texto)
print(match) # output: <re.Match object; span=(35, 66), match='Estava previsto para sair 16h30'>

print("\n")

print("Buscando por CPFs")
texto = """
Nome: Marcos | Idade: 30| CPF: 012.345.678-90 | País de origem: Brasil Nome: Ana | Idade: 28 |CPF: 098.765.432-10 | País de origem: Brasil Nome: Isadora | Idade: Não informado | CPF: 090.080.070-65 | País de origem: Brasil Nome: Guilherme| Idade: 21 | CPF: 111.222.333-45 | País de origem: Brasil """
padrao = '[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}' # Buscando CPFs no texto
match = re.search(padrao, texto)
print(texto)
match = re.search(padrao, texto)
print(f"re.search(padrao, texto) - Retorna apenas a posição do primeiro encontrado: {match}") # Retorna apenas a posição do primeiro encontrado
match2 = re.findall(padrao, texto)
print(f"re.findall(padrao, texto) - Retorna todos os encontrados em formato lista: {match2}") # Retorna todos os encontrados em formato lista