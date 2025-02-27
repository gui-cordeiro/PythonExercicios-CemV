times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia',
         'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino',
         'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Os 5 primeiros colocados: ')
for cont in range(0, 5):
    print(f'{cont + 1}º) {times[cont]} ', end="")

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Os 4 últimos colocados (Z4): ')
for cont in range(16, len(times)):
    print(f'{cont + 1}º) {times[cont]} ', end="")

print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Lista dos times em ordem alfabética:')
print(sorted(times))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Posição do Vasco da Gama (a.k.a. Gigante da Colina): ')
print(f'{times.index('Vasco da Gama') + 1}º colocado')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')