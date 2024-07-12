class Veiculo:
    def __init__(self, marca, modelo, cor, numero_rodas):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando....")
        print("Vhrummmm")
        
    def travar_rodas(self):
        print("Travando")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
        
class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, cor, numero_rodas, carregado):
        super().__init__(marca, modelo, cor, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
    
moto = Moto("BMW", "i9", "Azul e Branco", 4)
caminhao = Caminhao("Mercedes", "Sinotruck", "Prata", 10, True)

print(caminhao)
caminhao.esta_carregado()

print(moto)