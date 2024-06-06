import locale
pessoa = {"nome": "João", "idade": 32}
print(pessoa)

pessoa = dict(nome="Marcos", idade = 32)
print(pessoa)

#Criação de um dicionário aninhado

contactos = {
    "jose.martins@gmail.com": {"nome": "José", "telefone": "923698574"},
    "marta.martins@gmail.com": {"nome": "Marta", "telefone": "923697974"},
    "herculano.martins@gmail.com": {"nome": "Herculano", "telefone": "923698596"},
    "emilia.martins@gmail.com": {"nome": "Emília", "telefone": "923696374"},
}

# Dicionário misturado
dicionario = {'especie': 'Humano', 1: ['Obi Wan Kenobi', 'Qui-Gon Jinn']}
print(dicionario)

telefone = contactos["jose.martins@gmail.com"]["telefone"]
print(telefone)

#Utilizando a função zip para concatenar a chave:valor em um elemento do objeto dict:
dicionario = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
print(dicionario)

#Adição de nova chave - valor 

pessoa["telefone"] = "923698520"

print(pessoa)
print(pessoa.get('telefone'))

#Atualização de valor
pessoa["telefone"] = "+244923698520"
print(pessoa.get("telefone"))


locale.setlocale((locale.LC_MONETARY), "pt-BR.utf8")

carros_esportivos = {
    'ferrari': 2000000,
    'mercedes': 25000000,
    'mclarem': 15000000

}

#Comprehension
dicionario = {
    chave if valor > 1500000 else f'{chave}-valor-abaixo':
        f'{chave.upper()}: {locale.currency(valor, symbol=True)}'
        if valor > 10000000 else f'{chave.upper}: Valor abaixo de R$ 1.000.000, 00'
    for chave, valor in carros_esportivos.items()
}

print(dicionario)