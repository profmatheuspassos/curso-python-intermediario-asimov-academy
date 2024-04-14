filtro = filter(lambda x: x > 1, [1, 2, 3, 4])
print(list(filtro))

print("\n")

print(list(filter(lambda x: len(x) <= 3, ["asdfasdf", "asdfasdfasdf", "", "oi"])))

print("\n")

lista = ["abc", 1, 4, 6.5, ".", "22"]
print(listaOrdenada := sorted(lista, key = lambda x: len(x) if isinstance(x, str) else x))