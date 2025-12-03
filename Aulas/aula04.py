import os
os.system('cls')
os.system('color 6')

# IF ENCADEADO -> testa todas as condições MESMO SE uma for verdadeira
# ELIF -> testa todas as condições até UMA ser verdadeira

x = 15

if x <= 20:
    print('Entrou no if linha 11')
if x <= 15:
    print('Entrou no if linha 13')
if x <= 16:
    print('Entrou no if linha 15')

if x <= 20:
    print('Entrou no if linha 18')
elif x <= 15:
    print('Entrou no if linha 20')
elif x <= 16:
    print('Entrou no if linha 22')
# No caso de usar if ele vai testar todas as condições
# Se usar elif ele vai testar uma e sair da estrutura


    