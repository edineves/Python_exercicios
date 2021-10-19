#TABUADA V2
#Faça a tabuada mostrando a tabuada de um numero que o usuario escolher e use o For.
num= int(input('Digite um núnero para saber a tabuada  '))
for c in range (0,11):
    print(f' { num } x { c } = {num*c} ')
