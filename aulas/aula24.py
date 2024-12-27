# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  R o d r i g o
# -6-5-4-3-2-1 0

nome = 'Rodrigo'
print(nome[2])
print(nome[-4])
print('dri' in nome)
print('zero' in nome)
print(10 * '-')
print('Ro' not in nome)
print('go' not in nome)

nome2 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome2:
    print(f'{encontrar} está em {nome2}')
else:
    print(f'{encontrar} não está em {nome2}')