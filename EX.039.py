#ALISTAMENTO MILITAR
# Desenvolva um sistema, ao digitar a data de nascimento se o usuario for maior de 18 anos,
# apresentar a informação de alistamento militar.

from datetime import date
dt = int(input('Digite o ano de seu nascimento '))
atual = date.today().year
idade = atual - dt
# print(f'voce possui { idade }')
if idade >= 18:
    print(f' Sua idade é de {idade} anos e voce precisa se alista.')
else:
    print('Voce ainda ao precisa se alistar.')
