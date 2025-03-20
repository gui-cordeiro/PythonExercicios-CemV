# Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.  Guarde esses resultados
#               em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
#               número no dado.

from random import randint
from time import sleep
from operator import itemgetter

dadosJogador = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}

ranking = list()

print('-=' * 30)
print('Valores sorteados:')
for k,v in dadosJogador.items():
    print(f'\t - {k.capitalize()} tirou o valor {v} do dado!')
    sleep(0.5)

ranking = sorted(dadosJogador.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)

print('Ranking dos jogadores:')
for pos, valor in enumerate(ranking):
    sleep(0.5)
    print(f'\t {pos + 1}o. lugar: {valor[0]} - valor do dado {valor[1]}')

print('-=' * 30)