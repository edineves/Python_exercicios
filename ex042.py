#IMC
# Faça um programa onde o usuario digite o peso, altura e imprima o IMC com as informações necessárias

a = float(input('Digite sua altura '))
p = float(input('Digite o seu peso '))
imc = ( p/( a **2))
print(f'O seu IMC é {imc :.2f}')
if imc <= 18.5:
    print('magreza')
elif imc < 25:
    print('seu peso está normal ')
elif imc < 30:
    print(' Voce esta com sobrepeso')
else:
    print('Obesidade')