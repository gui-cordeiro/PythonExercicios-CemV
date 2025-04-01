# Exercício 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#               Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* tupla):
    print('-=' * 30)
    print('Analisando valores passados...')
    maiorValor = 0
    for valor in tupla:
        print(f'{valor} ', end='')
        if valor > maiorValor:
            maiorValor = valor
    print(f'Foram informados {len(tupla)} valores ao todo.')
    print(f'O maior valor informado foi {maiorValor}.')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()