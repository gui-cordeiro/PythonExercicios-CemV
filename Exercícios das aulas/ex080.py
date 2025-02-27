lita = list()
ultimo = True

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0:
        lita.append(valor)
        print('Adicionado ao final da lista!\n')
    if i >= 1:
        for lugar, dentro in enumerate(lita):
            # Valores ANTES do último
            if dentro > valor:
                lita.insert(lugar, valor)
                ultimo = False
                print(f'Adicionado na posição {lugar} da lista!\n')
                break
        # Maior valor, então irá para a última posição, caso o if de cima não deu certo
        if ultimo == True:
            lita.append(valor)
            print('Adicionado ao final da lista!\n')

        ultimo = True

print(f'\nLista final: {lita}')