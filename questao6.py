import os
os.system('cls')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = nota1 + nota2
media = soma / 2

if media >= 6:
    print('Parabéns! Aluno aprovado.')
elif media <= 4:
    print('Aluno está em recuperação.')
elif media < 4:
    print('Aluno reprovado.')
    
