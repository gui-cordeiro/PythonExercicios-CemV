# Exercício 086: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#                No final, mostre a matriz na tela, com a a formatação correta.

matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f'Insira um valor (posição {i + 1}x{j + 1}): ')))

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Matriz completa:')

for i in range(0,3):
    for j in range(0,3):
        print(f'[  {matriz[i][j]}  ]', end='')
    print('')