import os
os.system('cls')
# input
produto = input('Digite o nome do produto: ')
quantidade = int(input('Digite a quantidade do produto: '))
preco_unitario = float(input('Digite o preço: '))
# total
total = quantidade * preco_unitario
preço = total - quantidade
print(total)
if quantidade <= 5:
    desconto = total * 0.02
    print('Parabéns, você recebeu um desconto de 2%')
elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
    print('Parabéns, você recebeu um desconto de 3%')
elif quantidade > 10:
    desconto = total * 0.05
    print('Parabéns, você recebeu um desconto de 5%')

total_pagar = total - desconto
print(total_pagar)