# ***Dicts - Dicionários Python***
Os dicionários são coleções de itens e seus elementos são armazenados de forma não ordenada.Os dicionários Python são uma coleção que guarda valores multidimensionais para cada índice. Assim, é possível gerar estruturas mais complexas que simulam melhor a realidade e conseguem mapear instâncias do mundo real em um programa de software.

Seus elementos contém uma chave e valor, isto é:
* Uma `chave` que vai servir para indexar (posicionar) determinado elemento no dicionário.

* Um `valor` que contém… bem, um valor. Este valor aceita diversos tipos: listas, outros dicionários, inteiros, strings e etc.

Sua sintaxe básica é: `{'chave': 'valor'}`. Utiliza-se `{}` para delimitar o dicionário e a chave é separada do valor por dois pontos :.

## **Declaração e inicialização de conjuntos**

Para declarar e inicializar um dicionário em Python, existem as seguintes opções:
* **Dicionário Misturado**

![DicionarioMisturado](https://github.com/joao-nzuzi/trilha-python/assets/92062255/0a53e1ff-3c20-46dd-921f-10671436560e)

* **Dicionário Comum**

![dict normal](https://github.com/joao-nzuzi/trilha-python/assets/92062255/cac4e6b9-068a-4ed5-9ef6-d76dae447707)

* **Dicionário aninhado**

![dict aninhado](https://github.com/joao-nzuzi/trilha-python/assets/92062255/5a198bd3-029b-4259-b018-732225b58ab3)

* **Utilizando a função `zip` para concatenar a chave:valor em um elemento do objeto dict**

![dict zip](https://github.com/joao-nzuzi/trilha-python/assets/92062255/9432867a-28f2-41a7-bb33-23e79b35cb8c)

## **Adicionando Valores a um Dicionário**

Para adicionar ou atualizar valores a um dicionário em Python basta fazer da seguinte forma:
    
![AddUpdate](https://github.com/joao-nzuzi/trilha-python/assets/92062255/9e444511-128d-4dc3-a967-6441380bdda1)

> [!NOTE]
> Se a chave-valor informado não existe, então será feita uma adição ao dicionário. Caso contrário, o valor da chave informada será atualizado.

## **Removendo Valores de um Dicionário**

Para remover elementos de um conjunto em Python, também existem vários métodos disponíveis. Três dos métodos mais comuns são:

1. Método `pop('chave')`: Remove e retorna um elemento aleatório do dicionário.

![pop](https://github.com/joao-nzuzi/trilha-python/assets/92062255/577777c4-32bb-4722-9467-d247a36df533)

2. Método `popitem()`: Remove um par chave-valor aleatório.

![popitem](https://github.com/joao-nzuzi/trilha-python/assets/92062255/a26366e7-34b1-4bea-8be0-8281191f5e16)

3. Método `clear()`: Remove todos os pares chave-valor do dicionário.

![clear](https://github.com/joao-nzuzi/trilha-python/assets/92062255/7fed7e47-a3bd-440a-ad13-a6645f96002d)

4. Método `del`: Remove o par chave-valor informado.

![del](https://github.com/joao-nzuzi/trilha-python/assets/92062255/253fb37f-6cd8-4807-a843-af2491aaee81)
