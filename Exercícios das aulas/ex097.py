# Exercício 97: Faça um programa que tenha uma função chamada escreva(). que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    print('~' * 2 + '~' * len(texto) + '~' * 2)
    print(' ' * 2 + texto + ' ' * 2)
    print('~' * 2 + '~' * len(texto) + '~' * 2)

escreva("Curso em Vídeo - Mundo 3 de Python")
escreva("Guilherme, aka LinuxMan")
escreva("Devolve minha maçã (brincadeira :p)")