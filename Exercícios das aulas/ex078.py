valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont + 1} valor: ')))

maiorVal = valores[0]
menorVal = valores[0]

# Verificando o maior e o menor valor
for cont in valores:
    if cont > maiorVal:
        maiorVal = cont
    if cont < menorVal:
        menorVal = cont

maior = list()
menor = list()

# Verificando quantas vezes tais valores se repetem
for pos, cont in enumerate(valores):
    if maiorVal == cont:
        maior.append(pos)
    if menorVal == cont:
        menor.append(pos)

# Printando os resultados
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'O maior valor encontrado foi o {maiorVal} nas posições {maior}')
print(f'O menor valor encontrado foi o {menorVal} nas posições {menor}')



