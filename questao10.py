import os
os.system('cls')

print("""
     A-Álcool     | Até 25 litros, desconto de 2% por litro
                | Acima de 25 litros, desconto de 4% por litro
                
     G-Gasolina   | Até 25 litros. desconto de 3% por litro
                | Acima de 25 litros, desconto de 5% por litro
      """)

litros = int(input('Digite a quantidade de litros: '))
combustivel = input('Digite o combustivel: ').lower()
litro_gasolina = 6.59
litro_alcool = 3.79

if combustivel == 'a':
    total = litros * litro_alcool
if litros <= 25:
    desconto = total * 0.02
else:
    desconto = total * 0.04
    
if combustivel == 'g':
    total = litros * litro_gasolina
if litros <= 25:
    desconto = total * 0.03
else:
    desconto = total * 0.05

valor_pagar = total - desconto

print(f'Valor a pagar: R$ {valor_pagar:.2f}')

    
# desconto__ate_25_litros_alcool = litro_alcool * 0.02
# desconto__acima_25_litros_alcool = litro_alcool * 0.04
# desconto__ate_25_litros_gasolina = litro_gasolina * 0.03
# desconto__acima_25_litros_gasolina = litro_gasolina * 0.05
# if litros > 25 and combustivel == 'a':
#     total = litros * litro_alcool
#     print(total)
# elif litros < 25 and combustivel == 'a':
#     total = desconto__ate_25_litros_alcool
#     print(total)
# elif litros > 25 and combustivel == 'g':
#     total = desconto__acima_25_litros_gasolina
#     print(total)
# elif litros < 25 and combustivel == 'g':
#     total = desconto__ate_25_litros_gasolina
#     print(total)
    
# valor_pagar = total - desconto