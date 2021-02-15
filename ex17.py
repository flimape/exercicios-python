# Script realizado com Teorema de Pitágoras
import emoji
nome = input('Digite seu nome: ')
input(f'Saudações, {nome}!! Prazer em te conhecer!! Pressione qualquer tecla e dê enter para continuar.')
co = float(input('Digite aqui, em cm, o Cateto oposto do triângulo: '))
ca = float(input('Digite aqui, em cm, o cateto adjacente: '))
hipotenusa = (co**2 + ca**2) **(1/2)
print(f'O valor da hipotenusa é de {hipotenusa}cm ')
print(emoji.emojize('Muito obrigado por usar meu programa!! \n Te espero numa próxima, hein! :stuck_out_tongue_winking_eye:', use_aliases=True ))
input()