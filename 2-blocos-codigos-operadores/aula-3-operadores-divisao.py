# Operador piso (divisão inteira) - retorna a divisão sem a parte fracionária
print("Operador piso (divisão inteira) - retorna a divisão sem a parte fracionária - duas barras para a frente")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")

print("\n")

# Operador módulo (resto da divisão) - retorna o resto da divisão em unidades inteiras
print("Operador módulo (resto da divisão) - retorna o resto da divisão em unidades inteiras")
print(f"10 % 3 = {10 % 3}")
print(f"12 % 3 = {12 % 3}")

print("\n")

# Quando usar
print("Quando usar")
segundosTotais = 5749
minutos = segundosTotais // 60
segundos = segundosTotais % 60
print(f"Segundos totais: {segundosTotais}seg")
print(f"Convertido: {minutos}min {segundos}seg")

print("\n")

# Descobrir se o número é par
print("Descobrir se o número é par")
num = 6
par = (num % 2) == 0
print(f"O número {num} é par? {par}")