def exibir_hino_nacional(data_actual_extenso, *letra, **autores):
    texto = "\n".join(letra)
    meta_dados = "\n".join([f'{chave.title()}: {valor}' for chave, valor in autores.items()])
    mensagem = f'\n{data_actual_extenso}\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_hino_nacional(
    'Quinta-feira, 6 de Junho de 2022, 12:26',
    'Oh pátria nunca mais esqueceremos, os heróis de 4 de fevereiro',
    'Oh pátria nós saudamos os teus filhos, tombados pela nosso independência',
    'Horamos o passado e a nossa história, construimos no trabalho um homem nove',
    'Horamos o passado e a nossa história, construimos no trabalho um homem nove',
    'Angola avante, revolução, pelo poder popular',
    'Pátria unida, liberdade, um só povo uma só nação',
    'Angola avante, revolução, pelo poder popular',
    'Pátria unida, liberdade, um só povo uma só nação',
    'Levantemos nossas vozes libertadas',
    'Para a glória dos povos Africanos',
    'Marchemos combantentes angolanos, solidários com os povos oprimidos',
    'Orgulhosos lutaremos pela paz, com as forças progressistas do mundo',
    'Orgulhosos lutaremos pela paz, com as forças progressistas do mundo',
    'Angola avante, revolução, pelo poder popular',
    'Pátria unida, liberdade, um só povo uma só nação',
    'Angola avante, revolução, pelo poder popular',
    'Pátria unida, liberdade, um só povo uma só nação',
    autor = 'Manuel Rui', 
    compositor = 'Rui Mingas', data = '11 de Novembro de 1975'
)