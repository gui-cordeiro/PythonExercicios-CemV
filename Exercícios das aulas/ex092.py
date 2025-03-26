# Exercício 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
#               dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
#               e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#               OBS.: Considerar os 35 anos de contribuição como critério para aposentadoria.

from datetime import date;

dados = dict()

dados['nome'] = str(input('Digite seu nome: '))
dados['idade'] = date.today().year - int(input('Digite a data de nascimento: '))
dados['ctps'] = int(input('Digite a sua carteira de trabalho (0 caso não tenha): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite o seu salário: R$ '))
    dados['aposentadoria'] = 35 - (date.today().year - dados['contratacao']) + dados['idade']

print('-=' * 30)
print(dados)

for value in dados:
    print(f'"{value}" tem o valor "{dados[value]}"')
