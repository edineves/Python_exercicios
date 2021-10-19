#SORTEANDO UMA ORDEM NA LISTA
# Faça uma lista de alunos e apresente esta lista com os nomes e em seguida coloque esta lista em Ordem de Apresentação dos Trabalhos escolares
import random
from random import shuffle
a1 = str(input("Digite o seun nome "))
a2 = str(input("Digite o seun nome "))
a3 = str(input("Digite o seun nome "))
a4 = str(input("Digite o seun nome "))
a5 = str(input("Digite o seun nome "))
lista=[f'{a1}', f'{a2}', f'{a3}', f'{a4}', f'{a5}',]
escolhido = random.shuffle(lista)
print(f'A ordem de apresentação da lista é {lista} ')

