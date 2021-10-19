#NUMEROS PRIMOS
#Faça um programa que leia um numero digitado pelo uruario e informe na tela de seu computador se este numero é PRIMO ou não
def es_primo(num):
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False
print(es_primo(int(input('Digite um numero'))))