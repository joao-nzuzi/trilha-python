salario = 2500
def salario_bonus(bonus):
    # quando a variavel global nao é passada como argumento, então deve ser usada a palavra reservada global antes da variavel para que possamos usar ela dentro de uma função. Doutra forma a excepção UnboundLocalError: será lançada
    
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))