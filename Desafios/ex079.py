valores = list()
condicao = 'S'
while condicao != 'N':
    valor = int(input('Digite um valor: '))
    if not valor in valores:
        valores.append(valor)
        condicao = input('Deseja digitar um outro valor? [S/N]: ').upper()
    else:
        print('Este valor já existe na lista. Tente novamente.')

valores.sort()

print(valores)