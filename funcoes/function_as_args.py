def somar(a, b):
    return a + b

def subtrair (a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado é: {resultado}')
    
exibir_resultado(10, 20, somar)
exibir_resultado(10, 20, subtrair)