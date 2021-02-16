import emoji 
import playsound

nome = input('Digite seu nome: ')
input(f'Saudações, {nome}! Prazer em te conhecer!! \nPressione qualquer tecla e de enter para prosseguir')

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num// 1000 % 10

print('Analisando número...')
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar{m}')

print(emoji.emojize('Muito obrigado por usar meu programa!!! Te espero numa próxima, hein!:stuck_out_tongue_winking_eye:', use_aliases=True))
playsound.playsound('ahe.mp3')

input()