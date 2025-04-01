# Exercício 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, e realize a contagem.
#               Seu programa tem que realizar três contagens através da função criada:
#               a) De 1 a 10, de 1 em 1;
#               b) De 10 a 1, de 2 em 2;
#               c) Uma contagem personalizada.

from time import sleep

def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        fim += 1
    else:
        fim -= 1
        passo *= -1
    for valor in range(inicio, fim, passo):
        print(f'{valor} ', end='')
        sleep(0.5)
    print('FIM!')
    sleep(0.2)

contagem(1,10,1)
contagem(10,0,2)

print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
print('-=' * 30)



