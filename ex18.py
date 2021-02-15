import math
angulo = float(input('Digite o ângulo: '))
seno = math.cos(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.cos(math.radians(angulo))
print('O seno de {:.2f} é {:.2f}\n O cosseno é {:.2f} \n A tangente é {:.2f}' .format(angulo, seno, cosseno, tangente))
input()