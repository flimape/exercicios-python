nome = str(input('Digite seu nome completo: ')) .strip()
n = nome.split()
n1 = n[0]
n2 = n[len(n) - 1]
print(f'Seu primeiro nome é {n1}, e o último é {n2}')