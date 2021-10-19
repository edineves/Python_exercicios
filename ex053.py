#NUMEROS PRIMOS
#Faça um programa que identifique que o numero digitado é um numero PRIMO.
num = int(input('Digite um numero: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        total +=1
if total == 2:
    print(' é primo')
else:
    print('nao é primo')