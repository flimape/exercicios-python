import emoji
nome = input('Olá! Por favor, digite seu nome: ')
input('Saudações, {}! Prazer em te conhecer! Seja bem-vindo à sua tabuada.\n Para continuar, pressione qualquer tecla e dê enter. ' .format(nome))
n = int(input('Digite o número desejado: '))
print(f' {n} X {1} = {n*1} \n {n} X {2} = {n*2} \n {n} X {3} = {n*3} \n {n} X {4} = {n*4} \n {n} X {5} = {n*5} \n {n} X {6} = {n*6} \n {n} X {7} = {n*7} \n {n} X {8} = {n*8} \n {n} X {9} = {n*9} \n {n} X {10} = {n*10}')
print(emoji.emojize('Muito obrigado por usar meu programa!! \n Te espero numa próxima, hein! :stuck_out_tongue_winking_eye:', use_aliases=True))
input()