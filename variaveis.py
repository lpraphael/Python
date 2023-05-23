# Variáveis

# 1. Variáveis

age: int = 33 # Criando variável do tipo int

print("Idade: ", age)

name: str = 'Raphael'

altura: float = 1.78

estudando: bool = True

print('nome: ', name)
print(type(age))
print(type(name))
print(type(altura))
print(type(estudando))

'''
Tipos de variáveis:
    1. int: numéros Inteiros, ou seja, números sem parte decimal. Ex: 1, -5, 1000
    2. float: números reais, também chamados de ponto flutuante, ou seja, possuem parte decimal. Ex: 1.5, 3.14, 7.62
    3. str: cadeias de caracteres, ou seja, dados textuais. Ex: 'Hello World!' 
    4. bool: Valores lógicos (booleanos). Ex: True, False
'''

# Obtendo dados do usuário e guardando em uma variável.

linguagem: str = input('Qual linguagem você está estudando? ')

print('A linguagem que você está estudando é', linguagem)