nome = input('Olá! Digite seu nome: ')
print('Saudações, {}! Prazer em te conhecer!!' .format(nome))
input('Se quiser continuar para conversão R$ para dólar, pressione qualquer tecla para continuar')
rs = float(input('Digite o valor em real para saber sua conversão:R$ '))
v = rs / float(5.37)
print('{} reais equivale a {:.2f} dólares, na cotação do dólar do dia 12/2 de 2021.' .format(rs, v))
input('Para sair, basta pressionar qualquer tecla e dar enter')
