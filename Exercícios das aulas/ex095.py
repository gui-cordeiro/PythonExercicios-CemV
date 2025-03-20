# Exercício 95: Aprimore o exercício 93 para que ela funcione com vários jogadores, incluindo um sistema de visualização
#               de detalhes do aproveitamento de cada jogador.

fichaJogadores = list()
maxTamJogador = maxTamGols = 0

while True:
    jogador = dict()
    golsFeitos = list()
    print('-' * 30)
    jogador['nome'] = str(input('Nome do jogador: '))
    totPartidas = int(input(f'Quantas partidas {jogador['nome']} fez? '))
    for c in range(0, totPartidas):
        golsFeitos.append(int(input(f'\t => Quantos gols {jogador['nome']} fez na partida {c + 1}? ')))
    jogador['gols'] = golsFeitos[:]
    jogador['total'] = 0
    for c in range(0, len(jogador['gols'])):
        jogador['total'] += jogador['gols'][c]
    fichaJogadores.append(jogador.copy())
    del jogador, golsFeitos
    opt = str(input('Deseja continuar? [S/N]'))
    if opt == 'N' or opt == 'n':
        break

print('-=' * 30)
for f in fichaJogadores:
    if len(f['nome']) > maxTamJogador:
        maxTamJogador = len(f['nome'])
    if len(f['gols']) > maxTamGols:
        maxTamGols = len(f['gols'])

print(' Código' + (' ' * 5) + 'Nome' + (' ' * maxTamJogador) + 'Gols' + (' ' * maxTamGols) + 'Total')
print('-' * 50)
for pos, valor in enumerate(fichaJogadores):
    print(pos + (' ' * 10) + valor['nome'] + (' ' * maxTamJogador))
    # Continuar a tabela depois...

'''print('-=' * 30)
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
'''