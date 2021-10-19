#QUEBRANDO UM NUMERO
#Digite um numeo e mostre sua porcap inteira

from math import trunc   #funcao TRUNC em math que arredonda o numero

n = float(input('Digite um numero  '))
print(f'o valor digitado foi {n} e sua parte inteira é :',trunc(n))
