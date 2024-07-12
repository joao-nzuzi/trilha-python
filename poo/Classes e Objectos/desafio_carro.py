class Carro:
    
    def __init__(self, marca, modelo, cor, tipo_transmissao, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tipo_transmissao = tipo_transmissao
        self.ano = ano
    
    def buzinar(self):
        print("Pim Pim Pim")
    
    def ligar(self):
        print("Ligando")
        print("Carro ligado")
        
    def acelerar(self):
        print("Acelerando")
    
    def parar(self):
        print("Parando")
        print("Carro parado")
        
    # def __str__(self):
    #     return f'Carro: {self.marca}, {self.modelo}, {self.cor}, {self.tipo_transmissao}, {self.ano}'
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
mercedes = Carro("Mercedes", "Project One", "Prata", "Hibirido", 2023)
print(mercedes.marca, mercedes.modelo, mercedes.cor, mercedes.tipo_transmissao, mercedes.ano)
mercedes.ligar()
print(mercedes)