import random


numero = random.randrange(1,10)
escolha =  int(input('ecolha um número de 1 à 2000 --> '))


if numero == escolha:
    print('Você ganhou o jogo!🫵 😁 ')
    print('O numero aleatrorio é ', numero)
else:
    print('Errou feio! ☠️🧐')    
    print('O numero aleatrorio é ', numero)

