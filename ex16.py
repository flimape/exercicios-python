from math import trunc
nome = input('Digite seu nome: ')
input(f'Saudações, {nome}! é um prazer te conhecer!! Para continuar, pressione qualquer tecla e dê enter. ')
num = float(input('Digite um número real para saber sua parte inteira: '))
pr = trunc(num)
print(f'A parte inteira de {num} é {pr}')
input()