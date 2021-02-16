import playsound
import emoji
nome = input('Digite seu nome: ')
input(f'Saudações, {nome}! Prazer em te conhecer!! \nPara continuar, pressione qualquer tecla e de enter')
nc = input('Digite aqui deu nome COMPLETO: ')
ncupper = nc.upper()
nclower = nc.lower()
ncw = nc.replace(' ', '')
ncww = len(ncw)
n1 = nc.split()
n11 = n1[0]
n111 = len(n11)
print(f'Seu nome completo em maiúsculo é {ncupper} \nEm minúsculo é {nclower} \nSeu nome tem {ncww} letras \nSeu primeiro nome tem {n111} letras')
print(emoji.emojize('Muito obrigado por usar meu programa!! \nTe espero numa próxima, hein!:stuck_out_tongue_winking_eye:', use_aliases=True ))
playsound.playsound('ahe.mp3')
input()
