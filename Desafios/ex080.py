valores = list()

for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(valor)
        print('Adicionado ao final da lista!\n')
    else:
        for pos, c in enumerate(valores):
            if c > valor:
                valores.insert(pos, valor)
                print('Adicionado ', end='')
                if pos == len(valores):
                    print('ao final da lista!\n')
                else:
                    print(f'na posição {pos} da lista!\n')
                break
            elif pos == len(valores) - 1:
                valores.insert(pos + 1, valor)
                print('Adicionado ', end='')
                if pos == len(valores):
                    print('ao final da lista!\n')
                else:
                    print(f'na posição {pos + 1} da lista!\n')
                break

print(f'\nLista final: {valores}')