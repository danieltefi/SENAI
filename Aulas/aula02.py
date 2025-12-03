import os # Importa a biblioteca de sistema operacional

# Aula 02 -> Variáveis, tipos e input
# tipos de dados
# String -> texto (str)
# Int -> inteiro
# Float -> número quebrado

# Declaração de variáveis
escola = 'Senai'
print('O nome da minha escola é ' + escola) #mostra variável no print
print('O nome da minha escola é ',escola) # separando por parâmetro ','
# F string {} -> mostra o valor da variável dentro das aspas
print(f'O nome da minha escola é {escola}')

# Exemplo de variável int e float
numeroInteiro = 100
numeroQuebrado = 12.5
soma = numeroInteiro + numeroQuebrado

print('Somando numeroInteiro com 10', numeroQuebrado + 10)
print(f'Subtraindo numeroQuebrado com 5 = {numeroQuebrado -5}')
print(f'Somando numeroInteiro com numeroQuebrado = {soma}')
print('Multiplicando spma x2', soma*2)

os.system('cls') #limpa a tela (terminal)
os.system('color 2') #altera a cor no terminal p/ verde

# input('') -> pergunta algo ao usuário e armazema em uma variável
# Obrigatoriamente antes do input deve existir uma variável

escola = input('Digite sua escola: ')
print(f'Você estuda no(a) {escola}')

# Resumindo:
# input() -> pergunta algo ao usuário
# print() -> exibe algo ao usuário, mas não armazena valor

# Conversão de dados
# input() -> sempre armazena os valores em string
n = input('Digite um valor numérico: ')
print(type(n)) # Apresenta a tipagem

# int() -> converte ára número inteiro
# float() -> converte para números inteiros ou quebrados
# str() -> converte para texto (string)

n = int(input('Digite um valor numérico: '))
print('Tipo: ', type(n))

n = int(float('Digite um valor numérico: '))
print('Tipo: ', type(n))

n1 = float(input('Digite o primero número: '))
n2 = float(input('Digite o segundo número: '))
print(f'A soma de {n1} + {n2} é: {n1 + n2}')

# Porcentagem
print('25% de 100 =', 0.25*100)

# supondo que um produto custa 150 reais
# o caixa deu um desconto de 15%

desconto = 0.15 * 150
print(desconto)
print(150 - desconto)