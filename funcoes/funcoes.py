def hello_world():
    print("Hello, world")

hello_world()

def greeting():
    print("Olá, seja bem-vindo")

greeting()

def greeting(nome):
    print(f'Seja bem-vindo, {nome}')

greeting("João")

def greeting(nome='Anônimo'):
    print(f'Seja bem-vindo, {nome}')
    
greeting()