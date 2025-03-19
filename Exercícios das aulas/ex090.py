# Exercício 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#               No final, mostre o conteúdo da estrutura na tela.
#               OBS.: Considerar média 7,0.

aluno = dict()

aluno['nome'] = str(input('Digite o nome do(a) aluno(a): '))
aluno['media'] = float(input(f'Digite a média de {aluno['nome']}: '))

print(f'O nome do(a) aluno(a) é: {aluno['nome']}')
print(f'A média do(a) aluno(a) é igual a {aluno['media']}')
print('Situação: ', end='')
if aluno['media'] >= 7:
    print('APROVADO(A)')
else:
    print('REPROVADO(A)')