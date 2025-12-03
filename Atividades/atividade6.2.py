import random

nmaquina = ''
nusuario = 0

while nusuario != nmaquina:
    nmaquina = random.randint(0,10)
    nusuario = int(input('Tente adivinhar o número de 1 a 10: '))

    if nusuario == nmaquina:
        print('PARABÉNS! Acertou!')
        print(f'Seu número: {nusuario}')
        print(f'Número da máquina: {nmaquina}')
    else:
        print('Errou')
        print(f'Seu número: {nusuario}')
        print(f'Número da máquina: {nmaquina}')