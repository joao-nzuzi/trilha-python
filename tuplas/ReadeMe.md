# ***Tuplas - Tuple***

Uma tupla ( tuple ) em Python é uma sequência imutável de valores de qualquer tipo. Para criar uma tupla, lista-se uma sequência de valores separados por vírgulas e, opcionalmente, entre parênteses

## Declaração de tuplas
As tuplas em Python podem ser declaradas das seguintes formas:
* **Abrir parêntesis e separar os objectos por virgula (,)**
    * frutas = ("Banana", "Maçã", "Maracujá")
* **Palavra reservada tuple(). Nesta forma cada uma das letras representa um objecto e tem o seu índice**
    * letras = tuple("Python")
* **Matriz -> tuplas dentro da tupla**
    * matriz = (
        [1, "a", 2], 
        ["b", 3, 4],
        [5, 6, "c"]
        )
## Métodos de acesso e manipulação de tupla
* **count()** -> conta o numero de ocorrência de um objecto numa tuplas.
    * tupla_cores = ("Verde", "Azul", "Vermelho", "Verde", "Laranja")
    * print(tupla_cores.**count**('Verde'))
* **index()** - Pega a primeira ocorrência do objecto informado existente na dentro da tupla
    * linguagens_programacao.**index**("Java")

* **len()** -> exibe o tamanho do objecto
    * print(**len**(equipas_f1))

# ***Requisitos***
* Python
* VS Code ou qualquer editor de texto