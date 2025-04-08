# Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
   ano = 2025 - ano
   if ano < 16:
      return "VOTO NEGADO."
   elif ano < 18 or ano > 70:
      return "VOTO OPCIONAL."
   else:
      return "VOTO OBRIGATÓRIO."

print("-" * 30)
ano = int(input("Em que ano você nasceu? "))
print(f'Com {2025 - ano} anos: {voto(ano)}')