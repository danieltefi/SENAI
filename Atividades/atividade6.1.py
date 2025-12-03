i = 0

while i != 20:
    print(i)
    i = i + 1

c = 25

while c != 51:
    print(c)
    c = c + 1

nome ='' 
cpf = ''
idade = ''

print('1 = Nome, \n2 = CPF, \n3 = Idade, \n4 = Sair')
numero = 0

while numero <= 4:
    numero = int(input('Digite a opção desejada: '))

    if numero == 1:
        nome = input('Digite seu nome: ')
    elif numero == 2:
        cpf = input('Digite seu CPF: ')
    elif numero == 3:
        idade = input('Digite sua idade: ')
    elif numero == 4:
        print('Programa encerrado')
        break
else:
    print('Opção inválida! Digite um número de 1 a 4')

print('Dados cadastrados:')
print(f'{nome}, \n{cpf}, \n{idade}')