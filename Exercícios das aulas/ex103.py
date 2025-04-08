# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#                O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = "<desconhecido>", gols = 0):
   return f'O(A) jogador(a) {nome} fez {gols} gol(s) no campeonato.'

print('-' * 50)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

# Verificar se o valor de gols é válido
if gols.isnumeric():
   gols = int(gols)
else:
   gols = 0

if nome == '':
   print(ficha(gols = gols))
else:
   print(ficha(nome, gols))