import os
os.system('cls')

renda_mensal_do_solicitante = float(input('Digite a sua renda mensal: '))
valor_emprestimo = float(input('Digite o valor do emprestimo: '))
prestacoes = int(input('Digite quantas prestações: '))
valor_das_prestacoes = float(input('Digite o valor das prestações: '))

condicao1 = valor_emprestimo <= 10 * renda_mensal_do_solicitante
condicao2 = valor_das_prestacoes <= 0.30 * renda_mensal_do_solicitante

if condicao1 and condicao2:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo não concedido')
    