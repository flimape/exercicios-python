nome = input('Digite seu nome: ')
input(f'Saudações,{nome}! Prazer em te conhecer!! \n Pressione qualquer tecla e dê enter para continuar')
preço = float(input('Digite o preço do produto em reais: '))
desconto = preço * 0.05
final = preço - desconto
print(f'O preço do produto com 5% de desconto é {final} reais' )
input()
