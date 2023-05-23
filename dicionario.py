# > Dicionários.

# Criando Dicionários.

dicionario = {}
dicionario = dict()

dicionario = {
    'nome': 'Raphael',
    'idade': 33,
    'altura': 1.78
}

print(dicionario)

# Adicionando Elementos ao Dicionário.

dicionario['programador'] = True

print(dicionario)

# Alterando Elementos ao Dicionário.

dicionario['nome'] = 'Raphael Lyra Perazzo'

print(dicionario['nome'])
print(dicionario)

# Iterando sobre Dicionário.

for i in dicionario:
    print(i,': ', dicionario[i])

# Testando existência de uma chave

print('altura' in dicionario)   # Quando a chave existe no dicionário, retorna True
print('peso' in dicionario)     # Quando a chave não existe no dicionário, retorna False

print('Raphael Lyra Perazzo' in dicionario)
