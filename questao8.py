import os
os.system('cls')

print("""
     COR                |    PREÇO

      VERDE             |   R$ 10.00
      AZUL              |   R$ 20.00
      AMARELO           |   R$ 30.00
      VERMELHO          |   R$ 40.00
      """)

produto = input('Digite a cor: ')

if produto == 'verde':
    print('O preço é: R$ 10.00')
elif produto == 'azul':
    print('O preço é: R$ 20.00')
elif produto == 'amarelo':
    print('O preço é: R$ 30.00')
elif produto == 'vermelho':
    print('O preço é: R$ 40.00')
    