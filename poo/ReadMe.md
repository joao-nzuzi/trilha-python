# ***POO - Programação Orientada a Objecto***

## ***Classes***
As classes são uma forma poderosa de organizar e estruturar nosso código, permitindo a criação de objetos personalizados com propriedades e comportamentos próprios. No paradigma orientado à objetos, uma classe é a representação de algo do mundo real.

A utilização de classes é extremamente importante na programação orientada a objetos, pois permite a abstração de problemas complexos em entidades menores, além de facilitar a manutenção e reutilização do código.

No Python, podemos definir uma classe utilizando a palavra-chave `class`, seguida pelo nome da classe e por dois pontos `:` no final.

O nome da classe deve seguir algumas convenções, como começar com uma letra maiúscula e utilizar a notação CamelCase (iniciais das palavras compostas são maiúsculas e não há espaços ou underscores).

![classe](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/7016baa3-6e27-42fe-b241-486a9b68f657)


## ***Objectos***
Objetos são abstrações do Python para dados. Todos os dados em um programa Python são representados por objetos ou por relações entre objetos. Ou seja, em Python, todo valor é na verdade um objeto. Seja uma tartaruga, uma lista, ou mesmo um inteiro, todos são objetos.

## ***Construtor***
O construtor é um método especial que é executado automaticamente quando uma instância da classe é criada.

No Python, o construtor é chamado de `__init__`, que tem o `self` como o primeiro argumento.

Podemos utilizar o construtor para definir valores iniciais para os atributos da classe.

![construtor](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/68174e69-7ab0-4eb7-b45d-93709ea767b3)

> [!NOTE]
> `self`representa a instância de uma classe, e está sempre apontando para o objeto atual.

## ***Destrutor***

Em Python, um destrutor é um método especial qua é chamado quando um objecto está para ser destruído. É usado para performar ações de limpeza como fechar ficheirps, leberar recursos ou liberar memória. O construtor é chamado de `__del__`, que tem o `self` como o primeiro argumento.

![destrutor](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/c37ab238-21e8-406d-b1b0-9e175018c61c)

> [!NOTE]
> `self`representa a instância de uma classe, e está sempre apontando para o objeto atual.

## ***Herança***
Em programação herança é a capacidade que uma classe (filha) tem de herdar atributos / características e comportamentos de uma classe pai.

### ***Beneficios da herança***
* Representa bem o relacionamento do mundo real;
* Permite reutilização de código, evitando desse jeito a reescrita de códigos. Além disso, permite adicionar recursos numa classe sem precisar modificá-la.
* É de natureza transitiva, o que significa que se uma `classe B` herdar de uma `classe A`, todas as `classes` derivadas de `B` herdão a `classe A`.

#### ***Sintaxe de herança em Python***
A forma como se representa uma herança em python é passando a `classe pai`, neste exemplo a `classe A`, como argumento (dentro de parentesis logo após o nome da classe, neste caso a `classe B`) na `classe filha`, neste caso a `classe B`.

![heranca](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/5fe3e8c1-36c0-421a-9101-6345421f2a64)

#### ***Herança Simples***
É quando uma classe filha herda de apenas uma classe pai.

#### ***Herança Múltipla***
É quando uma classe filha herda de várias classes pai.

##### ***Sintaxe de herança multipla***
![heranca-multipla](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/c223ff0e-0c3f-424e-a094-862b3d5126a4)´

##### ***Super***
O uso do `super()` em herança múltipla é crucial para garantir que todos os métodos relevantes das classes base sejam chamados corretamente. O `super()` chama o próximo método na MRO, facilitando a chamada de métodos de superclasse de forma cooperativa.


## ***Encapsulamento***
Encapsulamento é a proteção dos atributos ou métodos de uma classe. Encapsulamento é proteger os dados dentro de um objeto, permitindo que apenas métodos específicos possam acessar ou modificar esses dados.

Em Python existem somente o public e o private e eles são definidos no próprio nome do atributo ou método.

Atributos ou métodos iniciados por no máximo dois sublinhados `__` e terminados por um sublinhado `_` são privados e todas as outras formas são públicas. *Essa conveção foi adoptada pela comunidade como forma de rápidamente identificar o que é privado e o que é público, visto que, diferente de linguagens como Java e/ou C++, python não tem palavras reservadas para identificar um atributo/método que privado ou publico*.

![encapsulamento](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/301f0f2e-e28f-4e1f-a24f-13f55ada2fdc)

No exemplo acima, a variável `_saldo` é privada pois obedece a a conveção definida pela comunidade, e todo acesso directo a ele funciona, no entanto fere o que foi convencionado pela comunidade

### ***Property*** 
Em Python, o decorador ``@property`` é usado para transformar um método em uma propriedade de uma classe.

Ele permite que um método seja acessado como atributo, sem a necessidade de chamá-lo como uma função.

![property](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/a09f885b-6665-47ce-8113-dbfc648fa8ec)

### ***Getters, Setters e Deleter***

Em muitos casos, queremos não apenas obter o valor calculado de uma propriedade, mas também definir seu valor.

Para isso, utilizamos os métodos `getter` e `setter`.

O método `getter` é responsável por retornar o valor da propriedade quando ela é acessada.

Utilizamos o decorador `@property` para definir o getter, como já vimos anteriormente.

O método `setter`, por sua vez, é usado para definir o valor da propriedade quando ela é modificada.

Para definir o `setter`, utilizamos o mesmo nome da propriedade seguido pelo decorador. Ex.: `@nomedapropriedade.setter`.

Além de obter e definir o valor de uma propriedade, também podemos excluí-la utilizando o método `deleter`.

Para definir o `deleter` de uma propriedade, utilizamos o decorador `@nomedapropriedade.deleter`.

![getter-setter](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/906af5af-ef52-48ee-b82b-ac1c47628bb9)

### ***Casos de uso do `@property`***
O decorador `@property` é muito útil em situações em que precisamos controlar o acesso aos atributos de uma classe.

Aqui estão alguns exemplos de casos de uso comuns:

- **Conversão de tipos**: podemos usar `@property` para converter automaticamente tipos de dados. Por exemplo, podemos ter um atributo data que é armazenado como uma string e uma propriedade data que devolve o valor convertido em um objeto datetime.

- **Verificação de validade**: podemos adicionar validações em um setter para garantir que os atributos estão dentro dos limites aceitáveis. Por exemplo, podemos ter um atributo idade que precisa ser um número positivo e, caso contrário, levanta um erro.

- **Uso de cache**: podemos utilizar uma propriedade para fazer cache de um valor calculado, evitando recalcular a cada vez que a propriedade é acessada.

- **Acesso a dados externos**: podemos usar propriedades para acessar e atualizar dados em bancos de dados externos ou sistemas remotos. Dessa forma, podemos manter a interface do objeto consistente, independentemente de onde os dados são armazenados.

## ***Polimorfismo***
Polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas (cuidado, polimorfismo não quer dizer que o objeto fica se transformando, muito pelo contrário, um objeto nasce de um tipo e morre daquele tipo, o que pode mudar é a maneira como nos referimos a ele).

Em Python, o polimorfismo é alcançado por meio do uso de métodos com o mesmo nome em diferentes classes, mas com implementações diferentes. Isso significa que um método pode ter comportamentos diferentes em classes diferentes, permitindo que o mesmo método seja chamado para objetos de diferentes classes, produzindo resultados diferentes.

O polimorfismo é especialmente útil quando se trabalha com herança. Por exemplo, considerando as classes Cachorro, Gato e Pássaro mencionadas anteriormente, todas elas podem ter um método chamado “emitir som”, mas cada uma delas pode ter uma implementação diferente desse método. Quando chamamos o método “emitir som” para um objeto de uma dessas classes, o comportamento será diferente dependendo da classe do objeto.

![polimorfismo](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/a6c41736-da36-45c4-b08c-d150794ad820)

### ***Classes Abstratas e Inteface***
Classes abstratas são aquelas que contém um ou mais métodos abstratos (métodos declarados, porém sem implementação — ou seja, somente a assinatura destes métodos sem corpo). Em Python, estas classes não podem ser instanciadas e precisam de subclasses que gerem implementação para os métodos, ou seja, as subclasses que herdam a classe abstrata devem sobrescrever obrigatoriamente seus métodos. São usadas apenas para serem herdadas, funcionando como uma superclasse e forçando hierarquia para todas as sub-classes.

Em Python, uma classe abstrata é definida utilizando o módulo “abc” e a classe `ABC` como base. Para declarar uma classe abstrata, é necessário decorá-la com o decorator `@abstractmethod`. Isso indica que os métodos decorados devem ser implementados nas classes filhas.

![class-abstract-interface](https://github.com/joao-nzuzi/sistema-bancario/assets/92062255/fdd4f83a-5847-4668-a51d-8e0b0c886753)