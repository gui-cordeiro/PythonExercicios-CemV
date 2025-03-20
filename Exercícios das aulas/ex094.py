# Exercício 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
#               dicionário e todos os dicionários numa lista. No final, mostre:
#                   a) Quantas pessoas foram cadastradas;
#                   b) A média de idade do grupo;
#                   c) Uma lista com todas as mulheres;
#                   d) Uma lista com todas as pessoas com idade acima da média.

cadastro = list()
somaIdades = 0

while True:
    ficha = dict()
    ficha['nome'] = str(input('Nome: '))
    ficha['sexo'] = str(input('Sexo [M/F]: '))
    ficha['idade'] = int(input('Idade: '))
    cadastro.append(ficha.copy())
    del ficha
    opt = str(input('Deseja continuar? [S/N]: '))
    if opt == 'N' or opt == 'n':
        break

print('-=' * 30)
print(f'- O grupo tem {len(cadastro)} pessoas no total;')
for c in range(0, len(cadastro)):
    somaIdades += cadastro[c]['idade']
mediaIdade = (somaIdades/len(cadastro))
print(f'- A média de idade é de {mediaIdade:.2f} anos;')
print(f'- As mulheres cadastradas foram: ', end='')

for c in cadastro:
    if c['sexo'] == 'F':
        print(f'{c['nome']} ', end='')

print(f'\n- Lista de pessoas que estão acima da média: ')
for c in cadastro:
    if c['idade'] > mediaIdade:
        print(f'\t => Nome = {c['nome']}; Sexo = {c['sexo']}; Idade = {c['idade']}.')
print('-=' * 30)