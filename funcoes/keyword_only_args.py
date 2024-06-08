
# Neste exemplo, tudo o que vem depois do asterisco * deve ser passado por keyword apenas.
def criar_carro(*, modelo, ano, marca, combustivel):
    print(f'{marca}, {modelo}, {combustivel}, {ano}')

criar_carro(modelo= 'Picanto', ano=2015, marca='Kia', combustivel='Gasolina')

# inválido. um erro será estourado
criar_carro('Picanto', 2015, 'Kia', 'Gasolina') 