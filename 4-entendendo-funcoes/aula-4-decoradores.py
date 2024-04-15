def func():
    return 2

minhaFuncao = func
retorno = minhaFuncao()
print(retorno)

def exibeFunc(f):
    print(f"Objeto de função recebido: {f}")
    print(f"Nome da função: {f.__name__}")

exibeFunc(func)

def funcExterna(x):
    def funcInterna(y):
        return x + y + 2
    return funcInterna

f = funcExterna(2)
print(f(2))