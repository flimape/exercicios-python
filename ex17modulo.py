# Script realizado com Teorema de Pitágoras
import emoji
import math
nome = input('Digite seu nome: ')
input(f'Saudações, {nome}!! Prazer em te conhecer!! Pressione qualquer tecla e dê enter para continuar.')
co = float(input('Digite aqui, em cm, o Cateto oposto do triângulo: '))
ca = float(input('Digite aqui, em cm, o cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é de {:.2f}cm ' .format(hi))
print(emoji.emojize('Muito obrigado por usar meu programa!! \n Te espero numa próxima, hein! :stuck_out_tongue_winking_eye:', use_aliases=True ))
input()