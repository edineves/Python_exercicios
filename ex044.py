#GERENCIAMENTO DE PAGAMENTOS
#Faça um programa que calcule o valor a ser pago com um preço normal e o preço em outra condição de pagamento caso o cliente queira parcelar
preco = int(input('Digite o preço do preço do produto R$ '))
print(F'Este é o valor a ser pago a vista { preco }, escolha outra forma de pagamento para novos proços')
opcao = int(input('Digite a forma de pagamento'"""
[ 1 ] a vista
[ 2 ] duas parcelas
[ 3 ] tres parcelas
[ 4 ] acima de quatro parcelas
"""))
if opcao == 1:
    print(f'O valor a vista será de R$ {preco},00')
elif opcao == 2:
    pc = preco+(preco*0.10)
    parcela = (pc/2)
    print(f'O valor da parcela sera de R$ { parcela }')
elif opcao == 3:
    pc = preco+(preco*0.08)
    parcela = (pc/3)
    print(f'O valor da parcela sera de R$ { parcela }')
elif opcao == 4:
    pc = preco + (preco * 0.06)
    parcela = (pc /4)
    print(f'O valor da parcela sera de R$ {parcela}')

print('OBRIGADO POR REALIZAR COMPRAS CONOSTO')






