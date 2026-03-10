import os
os.system('cls')

nome = input('Digite o seu nome: ')
genero = input('Digite o seu gênero: ')
estado_civil = input('Digite o seu estado civil: ')

if genero == 'feminino' and estado_civil == 'casada':
    tempo = float(input('Digite o tempo do seu casamento: '))
    print(f'Tempo de casada: {tempo}')

    
print(f'Nome: {nome} \n Gênero: {genero} \n Estado Civil: {estado_civil}')

