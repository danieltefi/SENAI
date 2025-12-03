votoc1 = 0
votoc2 = 0
votoc3 = 0
vencedor = ''

candidato1 = input('Digite um candidato: ')
ncan1 = int(input(f'Digite o número do candidato {candidato1}: '))

candidato2 = input('Digite outro candidato: ')
ncan2 = int(input(f'Digite o número do candidato {candidato2}: '))

candidato3 = input('Digite outro candidato: ')
ncan3 = int(input(f'Digite o número do candidato {candidato3}: '))

print('Participantes:')
print(f'Para votar em {candidato1} precione {ncan1}')
print(f'Para votar em {candidato2} precione {ncan2}')
print(f'Para votar em {candidato3} precione {ncan3}')

for i in range(10):
    voto = int(input(f'Digite seu {i + 1}º voto: '))
    if voto == ncan1:
        votoc1 = votoc1 + 1
        print(f'Voto computado para candidato {candidato1}')
    elif voto == ncan2:
        votoc2 = votoc2 + 1
        print(f'Voto computado para candidato {candidato2}')
    elif voto == votoc3:
        votoc3 = votoc3 + 1
        print(f'Voto computado para candidato {candidato3}')
    else:
        print('Candidato inexistente, voto anulado!')

if votoc1 > votoc2 and votoc1 > votoc3:
    vencedor = candidato1

elif votoc2 > votoc1 and votoc2 > votoc3:
    vencedor = candidato2

elif votoc3 > votoc1 and votoc3 > votoc2:
    vencedor = candidato3
else:
    print('Houve um empate, necessário novo turno!')

print(f'Candidato {candidato1} obteve {votoc1} votos')
print(f'Candidato {candidato2} obteve {votoc2} votos')
print(f'Candidato {candidato3} obteve {votoc3} votos')
print(f'Vencedor da votação:{vencedor}: ')