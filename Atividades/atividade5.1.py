for i in range(30, 48):
    print(i)

for i in range(0, -51,-1):
    print(i)

tabuada = int(input('Digite o número de uma tabuada: '))

print(f'Tabuada do {tabuada}:')

for i in range(1,11):
    print(f'{tabuada} x {i} = {tabuada * i}')