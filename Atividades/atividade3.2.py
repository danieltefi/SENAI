email = input('Digite seu e-mail: ')
senha = int(input('Digite sua senha: '))

if email != 'python@senai.com' or senha != 12345678:
    print('Usuário ou senha inválidos')
else:
    if email == 'python@senai.com' and senha == 12345678:
        print('Usuário autenticado')