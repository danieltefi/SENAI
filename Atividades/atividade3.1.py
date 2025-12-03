idade = int(input('Digite sua idade: '))

if idade <= 0 or idade >= 120:
    print('Idade inválida')
else:
    if idade >= 18 and idade < 120:
        print('Maior de idade')
    else:
        print('Menor de idade')
