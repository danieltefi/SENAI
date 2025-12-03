import os
os.system('cls')
os.system('color 6')

# FUNÇÕES
# Organizar o código e evitar a duplicidade
# def nomefuncao():
# A função só será executada ao ser chamada pelo nome

# FUNÇÃO SEM PARÂMETRO E FUNÇÃO SEM RETORNO

def Conteudo():
    print('Aula de funções')
    print('Estudando funções sem parâmetro e retorno')

Conteudo() # Chama a função para aparecer no código

# FUNÇÃO SEM PARÂMETRO E COM RETORNO

def FuncaoRetornaNumero():
    print('Essa função retorna o número 10')
    return 10 + 40
    # Após o comando return, a função não é mais executada

print(FuncaoRetornaNumero())
x = FuncaoRetornaNumero()
print(x)

def FuncaoExecutaNumero():
    print(100)

x = FuncaoRetornaNumero
y = FuncaoExecutaNumero

print(f'O valor de x: {x}')
print(f'O valor de y: {y}')

# Uma variável só irá armazenar o valor de uma função se a função tiver o comando return

# FUNÇÃO COM PARÂMETRO E SEM RETORNO

def ExecutaSoma(num1,num2):
    print(num1 + num2)

ExecutaSoma(15,20)

# Toda função com parâmetro ao ser chamada é obrigatório passar os parâmetros entre parenteses ()

# FUNÇÃO COM PARÂMETRO E COM RETORNO

def RetornaSoma(num1,num2):
    return num1 + num2

print(RetornaSoma(5,10))

# ESCOPO DE FUNÇÃO

numero = 100

def Escopo():
    print(numero)

print(numero)

Escopo()

# VARIÁVEIS DECLARADAS FORA DE UMA FUNÇÃO, SÃO CONSIDERADAS VARIÁVEIS GLOBAIS
# VARIÁVEIS DECLARADAS NO PARÂMETRO DE UMA FUNÇÃO OU DENTRO DE UMA FUNÇÃO, APENAS A FUNÇÃO ENXERGA

x = 10

def Exemplo():
    global x # O comando global serve para acessar variáveis fora da função
    x = 15

Exemplo()
print(x)