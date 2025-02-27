listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-----------------------------------')
print('        LISTAGEM DE PREÇOS         ')
print('-----------------------------------')
for cont in range(0, len(listagem), 2):
    print(f'{listagem[cont]}', end='')

    for dots in range(0, 26 - len(listagem[cont])):
        print('.', end='')

    if listagem[cont + 1] < 10:
        print('R$   ', end='')
    elif listagem[cont + 1] < 100:
        print('R$  ', end='')
    else:
        print('R$ ', end='')

    print(f'{f'{listagem[cont + 1]:.2f}'}')
print('-----------------------------------')