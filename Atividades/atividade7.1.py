def RetornaMult(n1,n2):
    return n1 * n2
    
print(RetornaMult(5,10))

dolar = ''
real = 0

def Dolar_Real():
    global dolar
    global real
    return dolar / 5.30

def Real_Dolar():
    global dolar
    global real
    return real * 5.30

print('*'*10, 'MENU', '*'*10)
print('Digite 1 para converter Dólar para Real, \nDigite 2 para converter Real para Dólar, \nDigite 3 para sair')
print('*'*26)

numero = 0

while numero <= 3:
    numero = int(input('Digite a opção desejada: '))

    if numero == 1:
        dolar = int(input('Digite o valor em Dólar: '))
        print(f'O valor em Real é: R$ {Dolar_Real()}')
    elif numero == 2:
        real = int(input('Digite o valor em Real: '))
        print(f'O valor em Dólar é: $ {Real_Dolar()}')
    elif numero == 3:
        print('Programa encerrado')
        break
else:
    print('Opção inválida! Digite um número de 1 a 3')