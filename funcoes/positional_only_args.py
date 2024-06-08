
# Neste exemplo, tudo o que vem antes da barra deve ser passado por posição apenas.
def criar_carro(modelo, ano, /, marca, combustivel):
    print(f'{marca}, {modelo}, {combustivel}, {ano}')

criar_carro('Picanto', 2015, marca='Kia', combustivel='Gasolina')

#Forma inválida. Um erro será estourado
criar_carro(modelo = 'Picanto', ano = 2015, marca='Kia', combustivel='Gasolina')