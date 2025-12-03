item1 = input('Digite um produto: ')
item2 = input('Digite outro produto: ')

valor1 = int(input(f'Digite o valor do produto {item1}: '))
valor2 = int(input(f'Digite o valor do produto {item2}: '))

desconto1 = 0.1 * valor1
desconto2 = 0.25 * valor2
total = (valor1 - desconto1) + (valor2 - desconto2)

print(f'O valor total da compra é: R${total}, \nDesconto produto {item1}: R${desconto1}, \nDesconto produto {item2}: R${desconto2}')