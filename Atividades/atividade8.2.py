respostas = {}

print('Responda com s para sim e n para não')
respostas['tel']= input('Telefonou para a vítima?: ').lower()
respostas['loc']= input('Esteve no local do crime?: ').lower()
respostas['mora']= input('Mora perto da vítima?: ').lower()
respostas['devia']= input('Devia para a vítima: ').lower()
respostas['trab']= input('Já trabalhou com a vítima?: ').lower()

print(respostas)

sim = 0
for resposta in respostas.values(): #pega apenas os valores de cada chave
    if resposta == 's':
        sim = sim + 1

if sim == 2:
    print('Suspeito')
elif sim >= 3 and sim <=4:
    print('Cúmplice')
elif sim == 5:
    print('Assasino')
else:
    print('Inocente')