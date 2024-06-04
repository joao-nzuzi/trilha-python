# ***Listas***

Em Python, as listas são um tipo de estrutura de dados que permite armazenar uma coleção de itens em uma única variável. As listas são mutáveis, o que significa que podem ser modificadas após serem criadas

## Declaração de lista
As listas em Python podem ser declaradas das seguintes formas:
* **Abrir colchetes e separar os objectos por virgula (,)**
    * frutas = ["Banana", "Maçã", "Maracujá"]
    * carro = ["Mercedes", "Class S", "2.500.000 USD", 2021, True]
* **Palavra reservada list(). Nesta forma cada uma das letras representa um objecto e tem o seu índice**
    * letras = list("Python")
    * numeros = list(range(10))
* **Matriz -> listas dentro da lista**
    * matriz = [
        [1, "a", 2], 
        ["b", 3, 4],
        [5, 6, "c"]
        ]
* **Comprehension - > criar uma lista a partir de um objecto iterável**
    * numeros = [1, 2, 3, 4, 10, 15, 6, 18, 90, 57]
    * pares = []
    * for numero in numeros:
        * if numero % 2  == 0:
            * pares.append(numero)
    * pares = [numero for numero in numeros if numero % 2 == 0]

## Métodos de acesso e manipulação de listas
* **append()** -> adiciona objecto na lista
    * Ex.: nome_lista.**append**(1), nome_lista.**append**("Python")
* **clear()** -> limpa a lista
    * Ex.: nome_lista.**clear()**
* **copy()** -> copia a lista para uma nova. A alteração de qualquer objecto na nova lista não afecta a lista da qual ela foi copiada.
    * segunda_lista = [1, "Python", [40, 30, 20]]
    * lista = segunda_lista.**copy()**
* **count()** -> conta o numero de ocorrência de um objecto numa lista.
    * lista_cores = ["Verde", "Azul", "Vermelho", "Verde", "Laranja"]
    * print(lista_cores.**count**('Verde'))
* **extend()** -> serve para juntar duas listas e não elimina valores duplicados
    * linguagens_programacao = ["Python", "Java", "Kotlin"]
    * linguagens_programacao.**extend**(["C#", "Js", "C++", "Java"])
* **index()** - Pega a primeira ocorrência do objecto informado existente na dentro da lista
    * linguagens_programacao.**index**("Java")

* **pop()** - Remove objecto na lista seguindo o padrão LIFO, excepto quando é informado o índice do objecto que se pretende remover
    * linguagens_progrmacao.**pop**()
    * linguagens_progrmacao.**pop**(0)

* **remove()** - Remove a primeira ocorrência do objecto que foi informado
    * linguagens_progrmacao.**remove**("Java")

* **reverse()** - Escreve a lista em ordem inversa
    * equipas_f1 = ["Mercedes", "Ferrari", "McLaren", "Aston Martin", "Red Bull Racing"]
    * equipas_f1.**reverse**()
    * print(equipas_f1)

* **sort()** - Organiza a lista em ordem alfabética, salvo se o reverse = True for informado
    * equipas_f1.**sort**()
    * print(equipas_f1)
    * equipas_f1.**sort**(reverse=True)
    * print(equipas_f1)

* **sort(key=lambda x: len(x))** -> ordena a lista pelo tamanho do objecto. Do menor para o maior.
    * equipas_f1.**sort(key=lambda x: len(x))**
    * print(f'\nOrdena a lista do menor para o maior:\n {equipas_f1}')

* **sort(key=lambda x: len(x), reverse=True)** -> ordena a lista pelo tamanho do objecto. Do maior para o menor
    * equipas_f1.**sort(key=lambda x: len(x), reverse=True)**
    * print(f'\nOrdena a lista do maior para o menor:\n {equipas_f1}')

* **len()** -> exibe o tamanho do objecto
    * print(**len**(equipas_f1))

* **sorted()** -> mesmo comportamento que o sort. O sorted é uma função built in
    * print (**sorted**(equipas_f1, key=lambda x: len(x)))
# ***Requisitos***
* Python
* VS Code ou qualquer editor de texto