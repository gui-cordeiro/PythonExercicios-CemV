# Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções
#                chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
#                e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
#                entre todos os valores PARES sorteados pela função anterior.

from random import randint

def sorteia(lista):
    numGerado = 0
    print(f'Sorteando 5 valores da lista: ', end='')
    for valor in range(0, 5):
        numGerado = randint(1,10)
        print(f'{numGerado} ', end='')
        lista.append(numGerado)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.', end='')

numeros = list()

sorteia(numeros)
somaPar(numeros)