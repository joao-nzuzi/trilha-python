lista = []

#Método append
lista.append(1)
lista.append("python")
print(lista)

#Metodo clear
lista.clear()
 
#Metódo copy
segunda_lista = [1, "Python", [40, 30, 20]]
lista = segunda_lista.copy()
print(lista)

#Metodo Count
lista_cores = ["Verde", "Azul", "Vermelho", "Verde", "Laranja"]
print(f"Nº de vezes que o verde se repete na lista: {lista_cores.count('Verde')}")

#Metodo extend -> serve para juntar duas listas e não elimina valores duplicados
linguagens_progrmacao = ["Python", "Java", "Kotlin"]
print (linguagens_progrmacao)
linguagens_progrmacao.extend(["C#", "Js", "C++", "Java"])
print(f"Lista extendida {linguagens_progrmacao}")

#Index - Pega a primeira ocorrência de um objecto dentro da lista
print(linguagens_progrmacao.index("Java"))

#Pop - Remove objecto na lista seguindo o padrão LIFO, excepto quando é informado o índice do objecto que se pretende remover
linguagens_progrmacao.pop()
linguagens_progrmacao.pop(0)
print(linguagens_progrmacao)

#remove - Remove a primeira ocorrência do objecto que foi informado
linguagens_progrmacao.remove("Java")
print(linguagens_progrmacao)

equipas_f1 = ["Mercedes", "Ferrari", "McLaren", "Aston Martin", "Red Bull Racing"]
#Reverse - Escreve a lista em ordem inversa
equipas_f1.reverse()
print(equipas_f1)

#Sort - Organiza a lista em ordem alfabética, salvo se o reverse = True for informado
equipas_f1.sort()
print(equipas_f1)
equipas_f1.sort(reverse=True)
print(equipas_f1)

#Sort(key=lambda x: len(x)) -> ordena a lista pelo tamanho do objecto. Do menor para o maior
equipas_f1.sort(key=lambda x: len(x))
print(f'\nOrdena a lista do menor para o maior:\n {equipas_f1}')

#Sort(key=lambda x: len(x), reverse=True) -> ordena a lista pelo tamanho do objecto. Do maior para o menor
equipas_f1.sort(key=lambda x: len(x), reverse=True)
print(f'\nOrdena a lista do maior para o menor:\n {equipas_f1}')

#len -> exibe o tamanho do objecto
print(len(equipas_f1))

#sorted -> mesmo comportamento que o sort. O sorted é uma função built in
print (sorted(equipas_f1, key=lambda x: len(x)))
