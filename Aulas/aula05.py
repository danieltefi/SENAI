import os
os.system('cls')
os.system('color 6')

# ESTRUTURA DE REPETIÇÃO FOR
# O número colocado no range é a quantidade de vezes a ser repetido
# por convenção usa-se a variável 1 no for, porém pode ser qualquer nome

# For com 1 parâmetro
for i in range(10):
    print('Hello World!') # imprime HELLO WORLD! 10x (i começa em 0 e vai até range -1 - de 0 a 9)
else:
    print('Acabou o for')

# For com 2 parâmetros:
for i in range(1,10): # i começa em 1 e vai até range -1 - de 1 a 09
    print(i)

# For com 3 parâmetros
for i in range(1,10,2): # i começa em 1, vai até range -1 e incrementa de 2 em 2 (1, 3, 5, 7, 9)
    print(i)

# É possivel também percorrer com negativos
for i in range(-10, -20,-1):
    print(i)

# ESTRUTURA DE REPETIÇÃO WHILE

