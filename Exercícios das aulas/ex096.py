# Exercício 96: Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area (a,b):
    print(f'A área de um terreno "{a:.1f}m" x "{b:.1f}m" é de "{(a*b):.1f}m²".')

print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)