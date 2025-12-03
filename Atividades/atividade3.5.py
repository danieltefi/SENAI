maca = int(input('Digite a quantidade de maçãs: '))
preco1 = 0.30
preco2 = 0.25

if maca <= 0:
    print('Quantidade de maçãs inválidas, digite um número maior ou igual a 1')
else:
    if maca <= 11:
        print(f'Você comprou {maca} maçã(s), o valor da compra é: R$ {maca * preco1}')
    else:
        print(f'Você comprou {maca} maçãs, o valor da compra é: R$ {maca * preco2}')