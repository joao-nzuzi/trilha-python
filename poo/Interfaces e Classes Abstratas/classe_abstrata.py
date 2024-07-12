from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando..... Ligada")
        
    def desligar(self):
        print("Desligando..... Desligada")
    

controlotv = ControleTV()
controlotv.ligar()
controlotv.desligar()
