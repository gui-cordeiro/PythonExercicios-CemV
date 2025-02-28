galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input(f'Nome {c + 1}: ')))
    dado.append(int(input(f'Idade {c + 1}: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'\nTemos {totmai} maiores e {totmen} menores de idade no total.')