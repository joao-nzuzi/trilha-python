class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_actual = 2024
        return _ano_actual - self._ano_nascimento
    
pessoa = Pessoa("João", 1992)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")