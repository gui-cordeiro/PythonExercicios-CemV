# Exercício 087: Aprimore o desafio anterior, mostrando no final:
#   a) A soma de todos os valores pares digitados;
#   b) A soma dos valores da terceira coluna;
#   c) O maior valor da segunda linha.

matriz = [[],[],[]]
num = somaPares = somaColuna = maiorLinha = 0

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Insira um valor (posição {i + 1}x{j + 1}): '))

        # Verificando se o número é par; se sim, soma com "somaPares"
        if num % 2 == 0: somaPares += num

        # Somando os valores da 3o. coluna
        if j == 2: somaColuna += num

        # Verificando se o valor digitado é o maior entre os valores da 2o. linha
        if i == 1 and num > maiorLinha: maiorLinha = num

        matriz[i].append(num)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Matriz completa:')
for i in range(0,3):
    for j in range(0,3):
        print(f'[  {matriz[i][j]}  ]', end='')
    print('')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print(f"a) Soma de todos os valores pares digitados: {somaPares}")
print(f'b) Soma dos valores da terceira coluna: {somaColuna}')
print(f'c) Maior valor da segunda linha: {maiorLinha}')