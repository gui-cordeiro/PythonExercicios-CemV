# Exercício 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
#               jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No
#               final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
golsFeitos = list()

jogador['nome'] = str(input('Nome do jogador: '))
totPartidas = int(input(f'Quantas partidas {jogador['nome'].capitalize()} fez? '))

print('-=' * 30)
for c in range(0, totPartidas):
    golsFeitos.append(int(input(f'\t => Quantos gols {jogador['nome'].capitalize()} fez na partida {c + 1}? ')))

jogador['gols'] = golsFeitos[:]

jogador['total'] = 0
for c in range(0, len(jogador['gols'])):
    jogador['total'] += jogador['gols'][c]

print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O campo nome tem o valor {jogador['nome']}')
print(f'O campo gols tem o valor {jogador['gols']}')
print(f'O campo total tem o valor {jogador['total']}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas, dentre elas:')
for c in range(0, len(jogador['gols'])):
    print(f'\t => Na partida {c + 1}, ', end='')
    if jogador['gols'][c] == 1:
        print(f'foi marcado apenas {jogador['gols'][c]} gol.')
    else:
        print(f'foram marcados {jogador['gols'][c]} gols.')
print('-=' * 30)
