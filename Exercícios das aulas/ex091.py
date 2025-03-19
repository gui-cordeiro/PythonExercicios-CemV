# Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.  Guarde esses resultados
#               em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
#               número no dado.

from random import randint
from time import sleep

dadosJogador = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}

print('Valores sorteados:\n')
for k,v in dadosJogador.items():
    print(f'\t - {k.capitalize()} tirou o valor {v} do dado!')
    sleep(1)

# Continua...