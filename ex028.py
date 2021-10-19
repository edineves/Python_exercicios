#JOGO DA ADVINHAÇÃO
#Dite um numero e o computador responderá se voce acertou ou nao o numero que foi escolhido.

from random import randint

n = int(input('Digite um numero inteiro entre 0 e 10 '))
computador = randint( 0,10 )
#print(f'Eu pensei no numero { n }')
#print(f'O computador pensou no numero {computador}')
if n == computador:
    print('Voce acertou ')
else:
    print(f'Nao foi desta vez, voce escolher o numero {n} e o computador o numero {computador}')