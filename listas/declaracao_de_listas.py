frutas = ["Banana", "Maçã", "Maracujá"]
print(frutas)
for fruta in frutas:
    print(fruta)
    
#Sabendo o indice da valor
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

letras = list("Python")
print(letras)
print(letras[2:])
print(letras[:2])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

numeros = list(range(10))
print(numeros)

carro = ["Mercedes", "Class S", "2.500.000 USD", 2021, True]
print(carro)

matriz = [
    [1, "a", 2], 
    ["b", 3, 4],
    [5, 6, "c"]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[-1][-1])

#comprehension com for
numeros = [1, 2, 3, 4, 10, 15, 6, 18, 90, 57]
pares = []
for numero in numeros:
    if numero % 2  == 0:
        pares.append(numero)
print(pares)

# Comprehension sofisticado
pares = [numero for numero in numeros if numero % 2 == 0]
print(f'Comprehension sofisticado:  {pares}')