numeros = {1,1,2,2,3,4,5,6}
print(numeros)

numeros = list(numeros) #converter set (conjunto) em lista
print (numeros[2])

conjunto_a = {1, 2, 3, 4, 6}
conjunto_b = {1, 2, 3, 4, 5}
print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_b))

conjunto_a.add(7)
print(conjunto_a)

conjunto_a.update([12, 20, 5])
print(conjunto_a)

conjunto_a.clear()
conjunto_a.copy()
conjunto_b.discard(1)
print(f"descartando {conjunto_b}")
conjunto_b.pop()
conjunto_a.remove(12)