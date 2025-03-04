# Exercício 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
#                No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
#                de cada aluno individualmente.

boletim = list()
opt = 'S'
lenMaiorNome = numAlunos = 0

while True:
    print(f'-=-=-=-=-=-=-=- Dados do {numAlunos + 1}o. aluno -=-=-=-=-=-=-=-')
    nome = input(">> Digite um nome: ")
    while True:
        nota1 = float(input('>> Digite a 1o. nota: '))
        if 0 <= nota1 <= 10: break
        else: print('[ERRO] Nota tem que ser entre 0 e 10.')
    while True:
        nota2 = float(input('>> Digite a 2o. nota: '))
        if 0 <= nota2 <= 10: break
        else: print('[ERRO] Nota tem que ser entre 0 e 10.')
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    if len(nome) > lenMaiorNome: lenMaiorNome = len(nome)

    opt = input('>> Aluno(a) registrado(a). Deseja inserir outro(a)? [S/N]: ')
    if opt == 'S' or opt == 's':
        print('')
        numAlunos += 1
    else:
        break

# Espaçamento padrão para tabela, caso o nome tenha menos de 3 letras
if lenMaiorNome < 3: lenMaiorNome = 3

print('\nCÓDIGO     NOME' + (' ' * lenMaiorNome) + 'MÉDIA' + (' ' * 5) + 'SITUAÇÃO')
for pos, valor in enumerate(boletim):

    # 1o. coluna: Código
    if pos < 100: print('0', end='')
    if pos < 10: print('0', end='')
    print(f'{pos + 1}', end='')
    if pos < 10: print(' ' * 8, end='')
    elif pos < 100: print(' ' * 7, end='')
    else: print(' ' * 6, end='')

    # 2o. coluna: Nome
    print(f'{valor[0]}', end='')
    if len(valor[0]) == lenMaiorNome:
        print('    ', end='')
    else:
        for c in range(lenMaiorNome - len(valor[0]) + 4):
            print(' ', end='')

    # 3o. coluna: Média
    print(f'{round(valor[2], 1)}', end='')
    if valor[2] != 10: print(' ', end='')

    # 4o. coluna: Situação
    if valor[2] < 7: print((' ' * 6) + 'Reprovado(a)')
    else: print((' ' * 6) + 'Aprovado(a)')

while True:
    opt = input('\n>> Deseja pesquisar o boletim de algum(a) aluno(a)? [S/N]: ')
    if opt == 'S' or opt == 's':
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        numPesquisa = int(input('>> Digite o código do(a) aluno(a): '))
        if numPesquisa > len(boletim): print("[ERRO] Código inválido.")
        else:
            for pos, valor in enumerate(boletim):
                if pos == numPesquisa - 1:
                    print(f'\n - Nome: {valor[0]}')
                    print(f'\t - Nota 1: {valor[1][0]}')
                    print(f'\t - Nota 2: {valor[1][1]}')
                    print(f' - Média: {round(valor[2], 1)}')
                    print(' - Situação: ', end='')
                    if valor[2] < 7: print('Reprovado(a)')
                    else: print('Aprovado(a)')
    else:
        break