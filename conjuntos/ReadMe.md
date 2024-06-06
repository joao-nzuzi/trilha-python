# ***Set - Conjuntos Python: A Coleção Sem Duplicações***
Os conjuntos são uma das estruturas de dados fundamentais em Python, conhecidos por sua capacidade de armazenar coleções de elementos exclusivos. Uma das principais características dos conjuntos em Python é que eles não permitem elementos duplicados. Isso significa que, ao adicionar valores a um conjunto, você pode ter certeza de que cada elemento será único.

## **Declaração e inicialização de conjuntos**

Para declarar e inicializar um conjunto em Python, existem as seguintes opções:
    ![create](https://github.com/joao-nzuzi/trilha-python/assets/92062255/eff06a38-a054-4d92-8e9b-038de868cc75)

## **Adicionando Valores a um Conjunto**

Para adicionar valores a um conjunto em Python, existem dois métodos principais que você pode usar: `add()` e `update()`.

- Método `add()`: Este método permite adicionar um único elemento ao conjunto. Se o elemento já estiver presente, o conjunto não será modificado.

    ![add](https://github.com/joao-nzuzi/trilha-python/assets/92062255/8679795a-3402-4043-ab45-82115abb5837)

- Método `update()`: Este método é usado para adicionar múltiplos elementos de uma vez. Você pode passar uma sequência (por exemplo, uma lista) como argumento, e os elementos dessa sequência serão adicionados ao conjunto:

    ![update](https://github.com/joao-nzuzi/trilha-python/assets/92062255/b2704c7b-17e6-4473-8cb9-35467465a9c9)

## **Removendo Elementos de um Conjunto**

Para remover elementos de um conjunto em Python, também existem vários métodos disponíveis. Três dos métodos mais comuns são:

1. Método `remove()`: Remove um elemento específico do conjunto. Se o elemento não estiver presente, ele levantará uma exceção `KeyError`.

2. Método `discard()`: Semelhante ao `remove()`, mas não gera uma exceção se o elemento não estiver presente. É útil quando você não tem certeza se o elemento está no conjunto.

3. Método `pop()`: Remove e retorna um elemento aleatório do conjunto. Tenha em mente que, como os conjuntos não têm ordem definida, o elemento removido será imprevisível.

![discard pop remove](https://github.com/joao-nzuzi/trilha-python/assets/92062255/a19e048d-3cbb-41bc-92ce-fbb9ac3d8ef3)

> [!NOTE]
> Lembre-se de que é importante usar esses métodos com cuidado, especialmente `remove()` e `discard()`, para evitar exceções indesejadas.
