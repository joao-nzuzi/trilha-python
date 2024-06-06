import locale

#Adição de nova chave - valor 

pessoa = {}
pessoa["telefone"] = "923698520"

print(pessoa)
print(pessoa.get('telefone'))

#Atualização de valor
pessoa["telefone"] = "+244923698520"
print(pessoa.get("telefone"))

contactos = {
    "jose.martins@gmail.com": {"nome": "José", "telefone": "923698574"},
    "marta.martins@gmail.com": {"nome": "Marta", "telefone": "923697974"},
    "herculano.martins@gmail.com": {"nome": "Herculano", "telefone": "923698596"},
    "emilia.martins@gmail.com": {"nome": "Emília", "telefone": "923696374"},
}

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

for chave, valor in contactos.items():
    print(chave, valor)
    
dict.fromkeys(["nome", "telefone"])
contactos.fromkeys(["Morada", "Sexo"], "Futungo")
print(contactos)

print(contactos.get("jose.martins@gmail.com"))

contactos.clear()

#Create a dict from a list using comprehension
lista = ["Ferrari", "Mercedes", "McLaren"]
lista_2 = []
dicionario = {
    f'Marca : {carro.lower()}':  f"Montadora: {carro.upper()}" for carro in lista
    }
print(dicionario)