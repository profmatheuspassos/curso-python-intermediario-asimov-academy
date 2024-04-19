import re
import datetime

print("Desafio 1 - encontrar datas")
def lerDatas(texto):
    padrao = '[0-9]{2}/[0-9]{2}/[0-9]{4}'
    datas = [
        datetime.datetime.strptime(dataStr, "%d/%m/%Y")
        for dataStr in re.findall(padrao, texto)
    ]
    return datas

texto = """
A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal.
"""

print(lerDatas(texto))

print("\n")

print("Desafio 2 - retorna a diferença de tempo")

def difTempo(inicio, fim):
    begin = datetime.datetime.strptime(inicio, "%H:%M:%S")
    end = datetime.datetime.strptime(fim, "%H:%M:%S")
    diferenca = end - begin
    horas, resto = divmod(diferenca.seconds, 3600) # Converte a diferença de tempo em horas
    minutos, segundos = divmod(resto, 60) # Converte a diferença de tempo em minutos e segundos
    return f"{horas:02}:{minutos:02}:{segundos:02}" # Formata a diferença como HH:MM:SS
    
inicio = '08:34:21'
fim = '13:55:09'
print(difTempo(inicio, fim))