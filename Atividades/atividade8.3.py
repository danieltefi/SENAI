import random

jogo1 = []
jogo2 = []

while len(jogo1)!= 6:
    jogo1.append(random.randint(1,60))
    jogo2.append(random.randint(1,60))

megasena = {}

megasena['jogo1']=jogo1
megasena['jogo2']=jogo2

print(megasena)