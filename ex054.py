#MAIORIDADE
#Faça um programa que onde o usuario ira digitar o ano de nascimento e o sisitema irá informar se
# a pessoa é maior ou não e quantas pessoas sao maiores e quantas são menores de idade.
from datetime import date
atual = date.today( ).year
maior = 0
menor = 0
for pessoa in range(1,5):
    nascimento = (int(input('Digite o ano de seu nascimento: ')))
    idade = atual-nascimento
    if idade > 18:
        maior += 1
        #print("voce é maior de 18 anos")
    elif idade<18:
        menor += 1
        #print('voce é menor de 18 anos')
print(f'O sistema identificou {maior} pessoas maiores de 18 anos e {menor} abaixo de 18.')

