# Exercício 95: Aprimore o exercício 93 para que ela funcione com vários jogadores, incluindo um sistema de visualização
#               de detalhes do aproveitamento de cada jogador.

fichaJogadores = list()
maxTamJogador = maxTamGols = 0

while True:
    jogador = dict()
    golsFeitos = list()
    print('-' * 30)
    jogador['nome'] = str(input('Nome do(a) jogador(a): '))
    totPartidas = int(input(f'Quantas partidas {jogador["nome"]} fez? '))
    for c in range(0, totPartidas):
        golsFeitos.append(int(input(f'\t => Quantos gols {jogador["nome"]} fez na partida {c + 1}? : ')))
    jogador['gols'] = golsFeitos[:]
    jogador['total'] = 0
    for c in range(0, len(jogador['gols'])):
        jogador['total'] += jogador['gols'][c]
    fichaJogadores.append(jogador.copy())
    del jogador, golsFeitos
    opt = str(input('Deseja continuar? [S/N]: '))
    if opt == 'N' or opt == 'n':
        break
print()
print(fichaJogadores)
print()
print('-=' * 30)
for f in fichaJogadores:
    if len(f['nome']) > maxTamJogador:
        maxTamJogador = len(f['nome'])
    if len(f['gols']) > maxTamGols:
        maxTamGols = len(f['gols'])

if maxTamJogador < 3: maxTamJogador = 4
if maxTamGols == 0: maxTamGols = 2

print('Código' + (' ' * 5) + 'Nome' + (' ' * maxTamJogador) + 'Gols' + (' ' * (maxTamGols * 3)) + 'Total')
print('-' * 60)
for pos, valor in enumerate(fichaJogadores):
    
    # 1° coluna: 
    if pos < 100: print("0", end='')
    if pos < 10: print("0", end='')
    print(f'{pos + 1}', end='')
    print(' ' * 8, end='')

    # 2° coluna:
    print(f'{valor["nome"]}', end='')
    if len(valor['nome']) == maxTamJogador:
        print(' ' * 4, end='')
    else:
        for c in range(0, maxTamJogador - len(valor['nome']) + 4):
            print(' ', end='')
    
    # 3° coluna:
    print(f'{valor["gols"]}', end='')
    if len(valor['gols']) == maxTamGols:
        print(' ' * 4, end='')
    else:
        for c in range(((maxTamGols - len(valor['gols'])) * 3) + 4):
            print(' ', end='')
    
    # 4° coluna
    print(f'{valor["total"]}')

print('-=' * 30)
while True:
    opt = input('\n>> Deseja pesquisar o desempenho de algum(a) jogador(a)? [S/N]: ')
    if opt == 'S' or opt == 's':
        print('-=' * 30)
        numPesquisa = int(input('>> Digite o código do(a) jogador(a): ')) - 1
        if numPesquisa > len(fichaJogadores): print("[ERRO] Código inválido.")
        else:
            print(f'\nO jogador {fichaJogadores[numPesquisa]["nome"]} jogou {len(fichaJogadores[numPesquisa]["gols"])} partidas, dentre elas:')
            for c in range(0, len(fichaJogadores[numPesquisa]['gols'])):
                print(f'\t => Na partida {c + 1}, ', end='')
                if fichaJogadores[numPesquisa]['gols'][c] == 1:
                    print(f'foi marcado apenas {fichaJogadores[numPesquisa]["gols"][c]} gol.')
                else:
                    print(f'foram marcados {fichaJogadores[numPesquisa]["gols"][c]} gols.')
    else:
        break
print('-=' * 30)