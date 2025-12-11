import os
os.system('cls')
os.system('color 6')

# Didionário
# Estruturas de dados
# Lista [] -> Realiza o armazenamento de mais de um tipo de dado e mais de um valor
# Tupla () -> Faz a mesma coisa que a lista, porém é imutável
# Dicionário {} -> Estrutura que armazena vários valores com as suas respectivas chaves

# declaração de um dicionário segue:
# dicionario = {key: value}

dicionario = {'professor': 'daniel', 'Qtd_anos': 10}

#Inserindo \ Alterando dados no dicionário
# se a chave nao existir, cria como nova
# se a chave existir, altera o valor
dicionario = {'item1': 'senai'}
print(dicionario)

# dicionario[key]=valune
dicionario['item2']='alunos'
dicionario[10]=99.99
dicionario['item2']='professores' #substitui o alunos por professores

print(dicionario)

# Excluindo item do dicionário
#pop(key) -> Remove pela chave
#clear() -> Limpa o dicionário inteiro

dicionario.pop('item2')
print(dicionario)

dicionario.clear()
print(dicionario)

# Exibindo valores do dicionário
#dicionario[key]
print(dicionario['item2'])

# percorrendo chaves e valores do dicionário
for key,value in dicionario.items():
    print(key,value,sep=':')

