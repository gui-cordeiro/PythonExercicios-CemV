# Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#                Ex: n = leiaInt('Digite um n')

def leiaInt(texto):
   while True:
      msg = input(texto)
      if msg.isnumeric():
         return msg
      else:
         print('\033[1:31mValor inválido. Tente novamente.\033[m')

n = leiaInt('Digite um n: ')
print(n)