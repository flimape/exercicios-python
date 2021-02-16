import playsound
import emoji
nome = str(input('Digite seu nome: '))
input(f'Saudações, {nome}! Prazer em te conhecer!! \nPara continuar, pressione qualquer tecla e de enter')

nc = input('Digite aqui deu nome COMPLETO: ')

ncupper = nc.upper()
nclower = nc.lower()

ncw = nc.strip()
ncw = ncw.replace(' ','')
ncw = len(ncw)

n1 = nc.split()
n1 = n1[0]
n1 = len(n1)

print(f'Seu nome completo em maiúsculo é {ncupper} \nEm minúsculo é {nclower} \nSeu nome tem {ncw} letras \nSeu primeiro nome tem {n1} letras')

print(emoji.emojize('Muito obrigado por usar meu programa!! \nTe espero numa próxima, hein!:stuck_out_tongue_winking_eye:', use_aliases=True ))

playsound.playsound('ahe.mp3')
input()
