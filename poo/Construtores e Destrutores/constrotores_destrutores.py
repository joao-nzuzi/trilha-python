class Cao:
    def __init__(self,nome, cor, raca):
        print("Inicializando a Classe")
        self.nome = nome
        self.cor = cor
        self.raca = raca
    
    def __del__(self):
        print("Removendo a instância da classe")
        
    def latir(self):
        print("auauau")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

def cadastrar_cao():
    cao = Cao("Piloto", "Castanho", "Rafeiro")
    print(cao)
    
cadastrar_cao()