# ***Set - Conjuntos***
Os conjuntos são uma das estruturas de dados fundamentais em Python, conhecidos por sua capacidade de armazenar coleções de elementos exclusivos. Eles são extremamente úteis quando você precisa garantir que não haja duplicação de dados e não se preocupa com a ordem em que esses elementos são mantidos.

## **Conjuntos Python: Uma Coleção Sem Duplicatas**

Uma das principais características dos conjuntos em Python é que eles não permitem elementos duplicados. Isso significa que, ao adicionar valores a um conjunto, você pode ter certeza de que cada elemento será único.

image

## **Adicionando Valores a um Conjunto**

Para adicionar valores a um conjunto em Python, existem dois métodos principais que você pode usar: `add()` e `update()`.

- Método `add()`: Este método permite adicionar um único elemento ao conjunto. Se o elemento já estiver presente, o conjunto não será modificado.

image

- Método `update()`: Este método é usado para adicionar múltiplos elementos de uma vez. Você pode passar uma sequência (por exemplo, uma lista) como argumento, e os elementos dessa sequência serão adicionados ao conjunto:

image

## **Removendo Elementos de um Conjunto**

Para remover elementos de um conjunto em Python, também existem vários métodos disponíveis. Três dos métodos mais comuns são:

1. Método `remove()`: Remove um elemento específico do conjunto. Se o elemento não estiver presente, ele levantará uma exceção `KeyError`.

2. Método `discard()`: Semelhante ao `remove()`, mas não gera uma exceção se o elemento não estiver presente. É útil quando você não tem certeza se o elemento está no conjunto.

3. Método `pop()`: Remove e retorna um elemento aleatório do conjunto. Tenha em mente que, como os conjuntos não têm ordem definida, o elemento removido será imprevisível.

image

Lembre-se de que é importante usar esses métodos com cuidado, especialmente `remove()` e `discard()`, para evitar exceções indesejadas.