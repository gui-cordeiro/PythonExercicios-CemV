# Exercício 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#   a) Quantas pessoas foram cadastradas;
#   b) Uma listagem com as pessoas mais pesadas;
#   c) Uma listagem com as pessoas mais leves.

ficha = list()
dados = list()
opt = 'S'
cont = maiorPeso = menorPeso = 0

while opt == 'S' or opt == 's':
    cont += 1
    ficha.append(str(input(f'Nome {cont}: ')))
    ficha.append(float(input(f'Peso {cont}: ')))
    if ficha[1] > maiorPeso: maiorPeso = ficha[1]
    if menorPeso == 0 or ficha[1] < menorPeso: menorPeso = ficha[1]
    dados.append(ficha[:])
    ficha.clear()
    opt = str(input('Deseja inserir mais uma pessoa? [S/N]: '))

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print(f'a) Total de pessoas cadastradas: {len(dados)}')
print(f'b) O maior peso registrado foi {maiorPeso:.1f}, referentes ao/à: ', end='')
for pos in range(0, len(dados)):
    if dados[pos][1] == maiorPeso:
        print(f'[{dados[pos][0]}] ', end='')
print(f'\nc) O menor peso registrado foi {menorPeso:.1f}, referentes ao/à: ', end='')
for pos in range(0, len(dados)):
    if dados[pos][1] == menorPeso:
        print(f'[{dados[pos][0]}] ', end='')