# > Estruturas Condicionais

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

'''
Imagine que você queira imprimir "aprovado(a)", caso o estudante tenha uma média superior
ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
'''

media: float = float(input('Digite a média de suas notas: '))
presenca: float = float(input('Digite a porcentagem de presença em aula: '))

if media >= 7 and presenca >= 70:
    print('aprovado!')
elif media >= 5 and presenca >= 70:
    print('Recuperação!')
else:
    print('Reprovado!')