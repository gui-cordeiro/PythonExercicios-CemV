tupla = ()

for cont in range(0, 4):
    num = int(input(f'Digite o {cont + 1}º número: '))
    tupla += (num,)

print(f'\n{tupla}')

print(f'O número 9 apareceu \'{tupla.count(9)}\' ', end='')
if tupla.count(9) == 1:
    print('vez.')
else:
    print('vezes.')

contador = 0

print('Posição do nº3: ', end='')
for pos in range(0, len(tupla)):
    if tupla[pos] == 3:
        contador += 1
        break

if contador == 0:
    print('Não encontrado')
else:
    print(tupla.index(3))

print(f'Números pares: ', end='')
for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(f'{tupla[cont]} ', end='')