# > Funções

# 1. O que são Funcões?
# são trechos de código encapsulado, que podem ser chamados/invocados em qualquer outra parte do programa
#Ex:
#   len()   -> Recebe uma lista como parâmetro e retorna o tamanho dessa lista.
#   print() -> Imprime uma mensagem no console (terminal/cmd).
#   input() -> Recebe um dado informado pelo usuário (entrada padrão).
#   min()   -> Recebe uma lista e retorna seu menor valor.
#   max()   -> Recebe uma lista e retorna seu maior valor.

# 2. Criação de funções:

# Função inicial

def saudacao():
    print('Seja bem vindo(a)!')
    print('Aqui você aprende a criar funções.')

saudacao()          # Aqui é a chamada da função, forma como a invocamos.
saudacao()          # A função pode ser invocada várias vezes no código.

# Função com parâmetros

def nova_saudacao(name):                 # Uma função pode receber parâmetros e trata-los dentro do seu escopo.
    print(f'Seja bem vindo(a), {name}!')
    print('Aqui nós aprendemos a criar funções usando parâmetros.')

nova_saudacao('Raphael')

# Função com parâmetros default

def nova_saudacao(name, course = 'Python'):                 # Uma função pode receber parâmetros e trata-los dentro do seu escopo.
    print(f'Seja bem vindo(a), {name}!')
    print(f'Aqui nós aprendemos a criar funções usando parâmetros default em {course}.')

nova_saudacao('Raphael')

# Função com retorno

def sum(num1, num2):
    return num1 + num2

result = sum(10, 15)

print('O resultado da soma é: ', result)