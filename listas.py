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

# Métodos e funções para manipular listas

new_list = [1, 3, 12, 8, 2]

# Append: Adiciona elemento ao final da lista

print('Antes do append: ', new_list)

new_list.append(3)

print('Depois do append: ', new_list)

# Insert: adiciona elemento em uma posição específica da lista

new_list.insert(2, 10) # insert(índice, elemento que quero add)

print('Depois do insert: ', new_list)

# Extend: Utilizado para unir duas listas. Pega os elementos da segunda lista e adiciona um a um ao final da primeira lista

new_list.extend(nova_lista3)

print('Depois do Extend: ', new_list)

# pop: Serve para remover o elemento especificado da lista, caso não especifique, remove o ultimo elemento da lista

print('Lista antes de remover elemento', new_list)

new_list.pop(0)

print('Lista após remover elemento na primeira posição: ', new_list)

new_list.pop()

print('Lista após remover último elemento: ', new_list)

# Remove: Utilizado para remover o primeiro elemento específicado da lista

print('Lista antes de remover elemento: ', new_list)

new_list.remove(3)

print('Lista após remover o primeiro elemento específicado: ', new_list)

# Count: Conta quantas vezes o elemento especificado aparece na lista

print('Quantidade de elementos "2" na lista: ', new_list.count(2))

# Index: Retorna o indice do elemento na lista

print('Índice do elemento 8 na lista: ', new_list.index(8))

# Sort: Ordena a lista

new_list2 = [3, 7, 1000, 25, 64, 78, 1, 0]

new_list2.sort()

print('Retorna a lista ordenada de forma crescente: ', new_list2)

# para retornar a lista ordenada de forma decrescente, é necessário utilizar dentro da função sort o parâmetro reverse = true

new_list2.sort(reverse=True)

print('Retorna a lista ordenada de forma decrescente: ', new_list2)

# Funções para Listas

# len: retorna a quantidade total de elementos da lista

print('Quantidade total de elementos da new_list2: ', len(new_list2))

# sum: Soma todos os elementos da lista

print('Valor da soma de todos os elementos da new_list2: ', sum(new_list2))

# max: Retorna o elemento com maior valor da lista

print('Maior valor entre todos os elementos da new_list2: ', max(new_list2))

# min: Retorna o elemento com menor valor da lista

print('Menor valor entre todos os elementos da new_list2: ', min(new_list2))

