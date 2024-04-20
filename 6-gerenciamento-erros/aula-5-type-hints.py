# Semelhante ao Swift --> PORÉM, ela não define os dados conforme o tipo indicado - veja último exemplo

x: int = 10
y: float = 5.5
nome: str = "Matheus"

nomes: list[str] = ["Luíza", "Henrique", "Ricardo"]

valores: tuple[int] = (1, 2, 3, 4)

produtos: dict[str, float] = {
    "carne": 4.4,
    "leite": 2.1
}

def somar(a: int, b: int) -> int:
    return a + b

print(somar(1, 2))
print(somar("Matheus", " é um bom professor"))