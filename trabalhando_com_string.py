texto = "PYtHon"
nome = "      José Matrins   "
idade = 25
profissao = "Progamador"

# dados_pessoais = {name: "Marcos José", age: 25, accupation : "Arquitecto de Software"}

print(texto.upper())
print(texto.lower())
print(texto.title())
print(nome.strip())
print(nome.lstrip())
print(nome.rstrip())
print("-".join(nome))
print(texto.center(10, "*"))


print(f'Olá, eu sou o {nome.strip()}, tenho {idade} anos de idade, e trabalho como {profissao}')

print(f'''
      
      ********* MENU MOVIMENTO BANCÁRIO *********
      1. Depositar
      2. Levantar
      3. Transferir
      4. Consultar
      5. Sair
      
      ''')