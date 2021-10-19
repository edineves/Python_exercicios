#COMPARANDO NUMEROS
#Digite dois numeros e o sistema deve analisar qual deles eh o maior e qual eh o menor.

n = int(input('Difite um numero  '))
n1= int(input('Digite outro numero '))
if n > n1:
    print(f' O numero { n } é maior que {n1}')
elif n == n1:
    print(f'O numero {n} é igual {n1}.')
else:
    print(f' O numero {n} é menor que {n1}.')
print('FIM')


