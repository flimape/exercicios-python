nome = input('Digite seu nome: ')
input('Saudações, {}! Prazer em te conhecer!! \n Nesta programação, irei te ajudar a calcular a área de sua paredee quantos litros de tinta precisará para pinta-la! \n Para continuar, pressione qualquer tecla e dê enter.' .format(nome) )
altura = float(input('Digite aqui, em metros, a altura de sua parede: '))
largura = float(input('Digite aqui, em metros, a largura de sua parede: '))
area = altura * largura 
tinta = area / 2
print('De acordo com as medidas da parede, a área total é {}, e precisará de {} litros de tinta' .format(area, tinta))
print('Obrigado por usar meu programa, volte sempre!')
input()