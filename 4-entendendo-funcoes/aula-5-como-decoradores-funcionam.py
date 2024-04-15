print("Ver detalhes no script\n")

def meuDecorador(func):
    def meuPacote(*args, **kwargs):
        # retorno = func(nome = nome)
        # return retorno.upper()
        return func(*args, **kwargs).upper()
    return meuPacote

@meuDecorador
def dizerOi(nome):
    return f"Olá, {nome}!"

# dizerOi = meuDecorador(func = dizerOi)


print(dizerOi("Matheus"))