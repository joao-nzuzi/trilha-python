class Animal:
    def __init__(self, numero_patas, numero_olhos, genero):
        self.numero_patas = numero_patas
        self.numero_olhos = numero_olhos
        self. genero = genero
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kargs):
        super().__init__(**kargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kargs):
        super().__init__(numero_patas = kargs["numero_patas"], numero_olhos = kargs["numero_olhos"], genero = kargs["genero"])
        self.cor_bico = cor_bico
        
class Cao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas, numero_olhos, genero):
        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, numero_patas = numero_patas, numero_olhos = numero_olhos, genero = genero)
        
        print(Ornitorrinco.__mro__) # Ornitorrinco.__mro__ / Ornitorrinco.mro()-> Python utiliza o Method Resolution Order (MRO) para determinar a ordem em que as classes são pesquisadas por métodos e atributos.

cao = Cao(cor_pelo= "Castanho", numero_patas = 4, numero_olhos = 2, genero = "Macho")
print(cao)

ornitorrinco = Ornitorrinco(cor_pelo="Castanho e preto", numero_patas = 4, numero_olhos = 2, genero = "Macho", cor_bico = "Preto" )

print(ornitorrinco)