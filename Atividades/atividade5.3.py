maiornumero = 0
for i in range(5):
        numero = float(input(f'Digite o {i + 1}º número: '))
        if numero > maiornumero:
            maiornumero = numero

print(f'maior número: {maiornumero}')