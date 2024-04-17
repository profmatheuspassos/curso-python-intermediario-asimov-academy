import datetime

data = datetime.date(2022, 1, 5)
print(data)
hora = datetime.time(18, 6, 30)
print(hora)
momento = datetime.datetime(2022, 1, 5, 18, 6, 36)
print(momento.strftime("Dia %d/%m/%Y, às %Hh%M."))
print(momento.strftime("Horário do log: " + "[%Y-%m-%d -- %H:%M:%S]"))
texto = "2023-12-31T08:45:30"
dataa = datetime.datetime.strptime(texto, "%Y-%m-%dT%H:%M:%S")
print(dataa)
textoo = "Aconteceu em 22/10/23 às 16h30min."
dataaa = datetime.datetime.strptime(textoo, "Aconteceu em %d/%m/%y às %Hh%Mmin.")
print(dataaa)
hoje = datetime.datetime.today()
print(hoje)
ano2000 = datetime.datetime(2000, 1, 1)
print(f"De 1 de janeiro de 2020 até hoje (17 de abril de 2024): {hoje - ano2000}")
print(f"Número de segundos totais: {(hoje - ano2000).total_seconds()}")