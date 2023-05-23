# > Listas

# Antes
nota1: float = 7.9
nota2: float = 9.7
nota3: float = 8.2

# Com Listas
lista: list[float]= [7.9, 9.7, 8.2]

# Criando listas

nova_lista1 = list()
nova_lista2 = []
nova_lista3 = [13, 'texto', 3.14159, True]
nova_lista4 = [[1, 2, 3], [4, 5, 6]]

print(nova_lista3[0])           # acessa o primeiro item da lista
print(nova_lista3[-1])          # acessa o ultimo item da lista
print(nova_lista3[0:3])         # Mostra os indices 0 , 1 e 2 da lista
print(nova_lista3[0:-1: 2])     # Mostra do primeiro elemento ao ultimo, pulando de 2 em 2

# Iteração com FOR

# Utilizando os próprios elementos da lista
for i in nova_lista3:
    print(i)

# Utilizando o índice
print('Imprime o comprimento da nova_lista3', len(nova_lista3))

for i in range(len(nova_lista3)):
    print(nova_lista3[i])




