# Exercício 106: Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

from time import sleep

def escreva(texto):
   """
   -> Imprime um texto com uma estilização básica.
   :param texto: O texto que será exibido
   :return: Nada.
   """
   print('~' * 2 + '~' * len(texto) + '~' * 2)
   print(' ' * 2 + texto + ' ' * 2)
   print('~' * 2 + '~' * len(texto) + '~' * 2)

escreva('SISTEMA DE AJUDA PyHELP')
while True:
   comando = str(input("Digite aqui o nome da função/biblioteca ('FIM' para encerrar): "))
   if comando.lower() == 'fim': break
   escreva('Acessando o manual do comando \'' + comando + '\'')
   sleep(1.5)
   help(comando)
escreva('ATÉ MAIS!')