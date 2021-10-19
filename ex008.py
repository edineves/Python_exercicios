#CONVERSOR DE MOEDAS
#Converta o valor em Reais que vc possui na carteira em Dolar,
# considerando a cotacao do Dolar de U$ 3,27.

reais = int(input('Digite a quantidade de Reais na carteira '))
dolar = 3.275535
valor= (reais * dolar)
print(f'O valor em R$ {reais},00 e em Dolar é U$ {valor :.2f} nesta data')

