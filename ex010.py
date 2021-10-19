#REAJUSTE DESCONTOS
#Calculando o novo preço de  um produto com um percentual de desconto

p = float(input('Digige o preço do produtto '))
d = float(input('Digite o desconto do produto '))
pn = p-(p*d)/100
print(f'O preço de {p} e com desconto de {d} no novo proço é R$ {pn}')