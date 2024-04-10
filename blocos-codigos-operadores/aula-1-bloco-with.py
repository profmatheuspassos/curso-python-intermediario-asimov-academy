import tempfile # Usado para criar diretórios ou arquivos temporários - usado no último exemplo
from pathlib import Path

pastaPadrao = Path(__file__).parent
pastaDestino = pastaPadrao / "notas"
pastaDestino.mkdir(exist_ok = True)

# Maneira "tradicional" e não recomendada de lidar com arquivos
arquivo = open(pastaDestino / "notas.txt", "w")
arquivo.write("Maneira \"tradicional\" e não recomendada de lidar com arquivos")
arquivo.close()

# Maneira recomendada - "context manager"
with open(pastaDestino / "notas2.txt", "w") as arquivo:
    arquivo.write("Maneira recomendada - \"context manager\"")
print("Arquivo foi fechado!")

# Criação de um diretório temporário
with tempfile.TemporaryDirectory() as tempDir:
    print(f"Diretório temporário criado: {tempDir}.")
    input()