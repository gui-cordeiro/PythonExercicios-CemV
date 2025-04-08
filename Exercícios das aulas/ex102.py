# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
   fatorial = 1
   if show: msg = ''
   for cont in range(num, 0, -1):
      if show:
         msg += f'{cont}'
         if cont != 1: msg += " x "
         else:
            msg += ' = ' + f'{fatorial}'
      fatorial *= cont
   if show: return msg
   else: return fatorial

print('-' * 30)
num = int(input('Digite um número para calcular o fatorial: '))
print(fatorial(num))
# print(fatorial(num, True))