import os
from pathlib import Path

print(os.getcwd())
print(os.listdir())

pasta = "5-explorando-biblioteca-padrao"

os.chdir(pasta)
print(os.getcwd())

caminho = Path(".")
print(caminho)
print(caminho.absolute())
print(list(caminho.iterdir()))
os.chdir("..")
print(os.getcwd())
