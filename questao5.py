import os
os.system('cls')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
operador = input('Digite o operador: ')

if operador == '*':
    print(f'{a * b}')
elif operador == '+':
    print(f'{a + b}')
elif operador == '-':
    print(f'{a - b}')
elif operador == '/':
    print(f'{a / b}')
    