#APROVANDO EMPRESTIMOS
#Faça um programa que aprove um emprestimo imobiliario considerando o valor do emprestimo e o seu salario, nao
# podendo ultrapassar 30% do seu salario a parcela.
imovel = float(input('Digite o valor do imvoel a ser financiado R$ '.strip()))
entrada = float(input('Digite o valor da entrada R$ '.strip()))
salario = float(input('Digite o seu salario bruto R$ '.strip()))
t = int(input('Quantos anos pretende financiar o imovel? '.strip()))
valor = imovel - entrada
taxa = 1
tempo = (t*12)
prestacao = (valor/tempo)
limitador = (salario*30)/100

if prestacao <= limitador:
    print(f'PARABENS seu financiamento foi aprovado para a compra do imovel')
else:
    print(f'No momento nao foi aprovado, consulte seu gerente')
print('OBRIGADO')

