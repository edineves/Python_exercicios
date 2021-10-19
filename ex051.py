#SOMA DOS NUMEROS IMPARES
#Faça um programa onde o usuario digite os dez numeros e o programa mostre a quantidade de numeros digitados e se estes forem impares a soma entre eles.
cont = 0
soma = 0
for c in range(0,5):
    num = int(input (f'Digite um numro'))
    if num % 3 == 0:
        soma += num
        cont += 1
print (f'Voce digitou {num} numeros IMPARES e a soma entre eles foi {soma}')