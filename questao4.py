import os
os.system('cls')

print("""
      
                        ATÉ 5 Kg             |          ACIMA de 5 Kg        
      
      
      Morango        R$ 2.50 por Kg         |      R$ 2.20 por Kg
      Maçã           R$ 1.80 por Kg         |      R$ 1.50 por Kg
      """)

maca = int(input('Digite a quantidade de maças em Kg: '))
morango = int(input('Digite a quantidade de morangos em Kg: '))

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20
if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

total = preco_morango + preco_maca
peso_total = morango + maca
valor_da_compra = total
print(valor_da_compra)

if maca or morango >= 10 or valor_da_compra > 15:
    total = total * 0.90
    print('Você recebeu 10% de desconto!')

