# ***Funções em Python***
Em Python, uma função é um bloco de código que realiza uma tarefa específica. Ela é definida usando a palavra-chave `def` , seguida pelo nome da função e parênteses. As funções oferecem uma maneira de organizar e reutilizar código, promovendo a legibilidade e a eficiência.

## **Declaração Funções**

Para declarar uma função em Python, existem as seguintes opções:
* **Função sem argumento**
![nor_args_function](https://github.com/joao-nzuzi/trilha-python/assets/92062255/fb4fb746-9ff4-472a-9ddf-cdc2657858b6)


* **Função com argumento**
![with_arg_function](https://github.com/joao-nzuzi/trilha-python/assets/92062255/d2991882-ac93-4e54-9a4c-be4e94282dae)

> [!NOTE]
> O argumento é informado dentro do parêntesis que precede o nome da função. Não existe um limite de argumentos que uma função pode/deve receber.


* **Função com argumento e valor predefinido**
![predefined-arg-function](https://github.com/joao-nzuzi/trilha-python/assets/92062255/41b8f84d-d680-4846-b450-11c353118b45)

> [!NOTE]
> O argumento e o valor do mesmo é informado dentro do parêntesis que precede o nome da função. Não existe um limite de argumentos que uma função pode/deve receber. Na chamada da função, se for informado um valor para o argumento, então, o valor predefinido será sobreescrito.

* **Função como argumento de uma função**
Em Python é possivel passar outra função como argumento de uma função, conforme a imagem abaixo
![function-as-args](https://github.com/joao-nzuzi/trilha-python/assets/92062255/989c99a8-acd5-4429-8ff0-0412deb67780)

* **Função com argumentos arbitrários (***args)**
Naquelas situações em que não se sabe o número de argumentos que deverão ser passados, python permite que se usa o `*` antes do nome da variável do argumento. Dessa forma, a função vai receber uma tupla como argumentos, e o acesso a eles é feito do mesmo jeito que se faz com a estrutura de dados tupla `tuple`

![Arbitrary Arguments](https://github.com/joao-nzuzi/trilha-python/assets/92062255/48f37413-1aaf-407e-af15-025c1628ba21)

* **Função com argumentos palavra-chave**

![kerword-as-arg](https://github.com/joao-nzuzi/trilha-python/assets/92062255/d38a800f-40ea-4a73-ac01-cc5a751c2fb3)

* **Função com argumentos palavras-chave arbitrários (****kargs)**
Se você não sabe quantos argumentos de palavra-chave serão passados ​​para sua função, adicione dois asteriscos: `**`antes do nome do parâmetro na definição da função.

![kargs](https://github.com/joao-nzuzi/trilha-python/assets/92062255/91350392-5f03-4f02-b71d-d0bd5bda35f8)

* **Função Reursiva**
Python também aceita recursividade, o que significa que uma função pode chamar ela mesma.

![recursividade](https://github.com/joao-nzuzi/trilha-python/assets/92062255/5a1d0e4d-c6e4-490e-9830-4c1b18a890e0)

> [!NOTE]
> O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escrever uma função que nunca termina ou que usa quantidades excessivas de memória ou potência do processador.

* **Função com arugumentos posicionais, palavra-chave e/ou mistas**
É possivel especificar que uma função pode ter APENAS argumentos posicionais ou APENAS argumentos de palavras-chave ou mistos.

- Para especificar que uma função pode ter apenas argumentos posicionais, adicione `, /` após os argumentos:

    ![positional-args-only](https://github.com/joao-nzuzi/trilha-python/assets/92062255/8f060169-89b4-476f-8c14-6aa33dbb3f68)

* Para especificar que uma função pode ter apenas argumentos palavra-chave, adicione `*,` antes dos argumentos:

    ![keyword-args-only](https://github.com/joao-nzuzi/trilha-python/assets/92062255/4bb7c958-af4e-4ee0-8dd6-a65441e25245)

* É possivel também combinar os dois tipos de argumentos na mesma função. Qualquer argumento antes de é `/` ,apenas posicional e qualquer argumento após é `*`, apenas de palavra-chave.

    ![combined](https://github.com/joao-nzuzi/trilha-python/assets/92062255/464bb906-ab87-4099-be33-7441054a45b2)

## **Retorno da função**
Em Python, a palavra reservada para indicar e/ou permitir que uma função retorne um valor é `return`. Importa dizer que diferente de linguagens como Java por exemplo que só retorna um único valor, python pode retornar múltiplos valores.

![retorno](https://github.com/joao-nzuzi/trilha-python/assets/92062255/b2508b52-196b-4a6c-84ec-00f61c6744aa)

