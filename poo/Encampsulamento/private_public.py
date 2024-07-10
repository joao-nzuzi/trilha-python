class Conta:
    
    def __init__(self, numero_agencia, saldo = 0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
        
    def depositar(self, valor):
        self._saldo += valor    
        
    def levantar(self, valor):
        self._saldo -= valor
    
    def mostar_saldo(self):
        return self._saldo
    

conta = Conta("0001", 100)
conta.depositar(1000)
print(conta.numero_agencia)
print(conta.mostar_saldo())

# Abaixo seguem as formas que ferem a coonveção da comunidade sobre atributos/metodos privados

print(conta._saldo)
conta._saldo += 100