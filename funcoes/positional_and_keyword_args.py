
#Os 2 primeiros são posicionais, e os 2 ultimos são por keyword

def criar_carro(modelo, ano, /, *, marca, combustivel):
    print(f'{marca}, {modelo}, {combustivel}, {ano}')

criar_carro('Picanto', 2015, marca = 'Kia', combustivel = 'Gasolina')

# inválido. um erro será estourado
criar_carro('Picanto', 2015, 'Kia', 'Gasolina')
criar_carro(modelo = 'Picanto', ano = 2015, 'Kia', 'Gasolina')
criar_carro(modelo = 'Picanto', ano = 2015, marca='Kia', combustivel='Gasolina')