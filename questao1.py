import os
os.system('cls')

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
soma = a + b

if soma > c:
    print('A e B são maiores que C')
else:
    print('São menores que C')