cadastro = {'Nome':'Dan', 'idade':33, 'Tel':'19 3521-5588', 'Endereço':'Av 40, nº 123'}
print(cadastro)

print(cadastro['Nome'])

d = {}

nome = input('Digite seu nome: ')
d['nome']=nome
idade = int(input('Digite sua idade: '))
d['idade']=idade
telefone = input('Digite seu telefone: ')
d['telefone']=telefone
endereco = input('Digite seu endereço: ')
d['endereco']=endereco

print(d)

for key,value in d.items():
    print(key,value,sep='...')