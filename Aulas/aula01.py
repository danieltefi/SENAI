# Aula 01 - Exibindo mensagens no terminal com print('')
# Tipos de dados
# String (texto) -> sempre entre aspas ('')
# Int, float (inteiro, nº quebrados) -> sem aspas (x)

print('Oi mundo!') #texto (str)
print(10) # nº inteiro (int)
print(5.99) # nº quebrado (float) -> sempre ponto (x.x)

# Operações matemáticas + - / *
print("10" + "10") # Somando texto (concatenação)
print(10 + 10) # Somando número

# Parâmetros no print
# print(a,b,c,d,e...) até 128 parâmetros
print('Escola SENAI') # 1 parâmetro
print('Escola', 'SENAI') # 2 parâmetro (separados por vírgula)

# Formatações Sep e End -> Final do print
# Sep -> Operador de separação (troca o caracter ',' por outro caracter)
# End -> Operador final (coloca o caracter no final do print)

# Sep *Obrigatório usar parâmetros
print('Hoje', 'é', 'dia', '06')
print('Hoje', 'é', 'dia', '06', sep=' ! ')

# End -> Coloca o caracter no final e deixa os prints na mesma linha
# \n -> Quebra linha
print('Curso de Python', end=' no SENAI') # precisa colocar o espaço antes para não emendar com a palavra anterior
print(' aprendendo operadores no print') # coloca a frase tudo junto em um print só (colocar espaço também)
#print('\naprendendo operadores no print') # quebra a linha, aparecendo como outro print

# usando Sep e End no mesmo print
print('Cade', 'minha', 'mesa com regulagem de altura', sep='*()*', end=' espero que comprem!\n')

# Formatação
print('*'*10, 'Loja do SENAI', '*'*10) # Adiciona 10 *