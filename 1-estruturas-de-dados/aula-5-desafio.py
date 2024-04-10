print("DESAFIO 1")
print("Converta o loop abaixo para uma compreensão de lista")
valores = [30, 50, 100, 120]
triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)
print(triplos)
print("Compreensão em lista")
triplos2 = [valor * 3 for valor in valores]
print(triplos2)

print("\n")

print("DESAFIO 2")
palavras = ['Olá', 'Python', 'Juliano', 'Asimov Academy']
dicionarioPalavras = {
    palavra.lower(): len(palavra.replace(" ",""))
    for palavra in palavras
}
print(dicionarioPalavras)

print("\n")

print("DESAFIO 3")
gostamProgramacao = {"Ricardo", "Roberto", "Pedro", "Vinicius"}
gostamFutebol = {"Mateus", "Roberto", "Paulo", "Vinicius"}
estudamAsimovAcademy = {"Ricardo", "Mateus", "Paulo", "Pedro"}
print(gostamProgramacao.intersection(estudamAsimovAcademy).difference(gostamFutebol))
print((gostamProgramacao & estudamAsimovAcademy) - gostamFutebol)