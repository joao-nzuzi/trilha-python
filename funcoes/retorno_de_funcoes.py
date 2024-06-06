
def calcular_O_total_da_lista_iinformada(numeros):
    return sum(numeros)

def calcular_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 2
    return antecessor, sucessor

lista_numeros = [1, 3, 5, 52]

print(calcular_O_total_da_lista_iinformada(lista_numeros))
print(calcular_antecessor_sucessor(50))