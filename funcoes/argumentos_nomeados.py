def carro(marca, modelo, ano_fabrico):
    print(f'Carro inserido com sucesso -> Marca: {marca}, Modelo: {modelo}, Ano de Fabrico: {ano_fabrico}')

carro("Kia", "Picanto", 2015)

# Com esta forma, mesmo que a ordem dos argumentos infomados sejam diferentes da declarada na função, os valores serão inseridos obedecendo a ordem declarada na função
carro(**{'modelo': 'Picanto', 'ano_fabrico': 2015, 'marca': 'Kia'})