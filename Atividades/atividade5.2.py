quantidade = int(input('Digite a quantidade de pães: '))
preco = 0.18
total = (quantidade * preco)
paomucho = (total * 0.1)
totaldesc = (total - paomucho)

for i in range(1,51):
    print(f'{i} pães: Você deve pagar R$ {i * preco:.2f}')

print(f'Total da compra sem desconto R$ {total:.2f}')

cupom = input('Possui cupom de desconto? insira o cupom: ').lower()
pagamento = int(input('Qual o método de pagamento? (apenas valor): NOTA 2, NOTA 5, NOTA 10 ou NOTA 50? '))

if cupom == 'paomucho':
    print(f'Desconto aceito. Desconto de 10%. Total com desconto: R${totaldesc:.2f}')
    if pagamento > totaldesc:
         print(f'Troco de R$ {pagamento - totaldesc:.2f}')
    elif pagamento < totaldesc:
        print(f'Dinheiro insulficiente. Faltam R$ {totaldesc - pagamento:.2f}')
    else:
        print('pagamento OK!, não há troco')
else:
    print('Desconto inválido')
    if pagamento > total:
        print(f'Troco de R$ {pagamento - total:.2f}')
    elif pagamento < totaldesc:
        print(f'Dinheiro insulficiente. Faltam R$ {total - pagamento:.2f}')
    else:
        print('pagamento OK!, não há troco')