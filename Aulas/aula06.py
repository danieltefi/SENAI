import os
os.system('cls')
os.system('color 6')

# Estrutura de repetição While (enquanto)
# Enquanto uma condição for verdadeira ele executa o looping até que ela seja falsa
# Por se tratar de uma condição, você deve usar os operadores condicionais
# Operadores: < > <= >= == != and e or

aula = 6

while aula == 6:
    print('Apredendo while')
    aula = 7
    # break -> quebra o loop (igual ao definir aula = 7)
else:
    print('Acabou o while')

# Para sair do while a condição deve ser falsa ou utilizar a palavra break

# while incremental

i = 0

while i != 11:
    print(i)
    i = i + 1 # incrementando uma variável por extenso (abreviado = i += 1)

import random

for i in range(5):
    numero = random.randint(0,5) # Gera um número aleatório entre 0 e 5
    print(numero)

