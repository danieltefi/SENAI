nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2) / 2

if media < 5:
    print(f'Sua média é {media}, voce está reprovado')
elif media >= 5 and media < 7:
    print(f'Sua média é {media}, voce está de recuperação')
else:
    print(f'Sua média é {media}, voce está aprovado')


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 17:
    print(f'Seu IMC é {imc}, você está muito abaixo do peso')
elif imc >= 17 and imc <= 18.49:
    print(f'Seu IMC é {imc}, você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.99:
    print(f'Seu IMC é {imc}, você está com peso normal')
elif imc >= 25 and imc <= 29.99:
    print(f'Seu IMC é {imc}, você está acima do peso')
elif imc >= 30 and imc <= 34.99:
    print(f'Seu IMC é {imc}, você está com obesidade I')
elif imc >= 35 and imc <= 39.99:
    print(f'Seu IMC é {imc}, você está com obsesidade II (severa)')
else:
    print(f'Seu IMC é {imc}, você está com obsesidade III (mórbida)')