import random

numero_sorteado: int = random.randint(1, 10)

numero: int = 0
contador: int = 0

while numero != numero_sorteado:
    if numero != 0:
        print('')
        print('Você errou, tente novamente')

    numero: int = int(input('Digite um número de 1 a 10: '))
    contador += 1

print('O número sorteado foi: ', numero_sorteado)
print('você deu', contador, 'palpites antes de acertar!')