# > Conversão de Tipos

numero1: str = '10'
numero2: str = '20'
idade: int = 33
print(numero1 + numero2)
print(numero1, type(numero1))
print(idade)
numero_inteiro = int(numero1)
print(numero_inteiro, type(numero_inteiro))
print(type(str(idade)))

# int() -> converte a variavel para o tipo int
# str() -> converte a variavel para o tipo str
# float() -> converte a variavel para o tipo ponto flutuante (float)
# bool() -> converte a variavel para o tipo booleano

# É possível utilizar essas funções em conjunto com outras

# Por padrão, a função input() sempre captura a informação no formato str
numero3 = int(input('digite um número: '))

print(numero3, type(numero3))