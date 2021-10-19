#PAR OU IMPAR
# Faça um programa onde o usuario digita um numero e no final apresente se o numero é par ou impar

n = int(input('Digite um numero '))
if n % 2 == 0:
    print(' O numero é par')
else:
    print(f' O numero digitado foi {n} e é um numero impar')