# Exercício 088: Faça um programa que ajude um jogador da MEGA-SENA a criar palpites. O programa vai perguntar quantos
#                jogos serão gerados e vai sortear 6 números entre 1 e 60 para cara jogo, cadastrando tudo em uma lista
#                composta.
from time import sleep
from random import randint

num = numGerado = contBolao = contAposta = 0
valorExisteNaLista = False
bolao = list()
aposta = list()

print('+-------------------------------+')
print('| GERADOR DE JOGOS DA MEGA-SENA |')
print('+-------------------------------+')

while num <= 0:
    num = int(input(">> Digite quantas apostas da Mega-Sena você deseja criar: "))
    if num <= 0: print("\t[ERRO] Você inseriu um valor igual ou inferior a 0. Tente novamente.\n")

while contBolao < num:
    while contAposta < 6:
        numGerado = randint(1,60)

        # Verificando se o valor gerado já existe na lista atual; se sim, será descartado. Se não, será implementado.
        if numGerado not in aposta:
            aposta.append(numGerado)
            contAposta += 1

    # Organizando os números da aposta e inserindo na lista de apostas
    aposta.sort()
    bolao.append(aposta[:])
    aposta.clear()

    # Ajustando variáveis de "controle"
    contBolao += 1
    contAposta = 0

# Mostrando os resultados
print(f"\n-=-=-=- SORTEANDO {num} JOGOS -=-=-=-")
sleep(1)
for numJogo, aposta in enumerate(bolao):
    print(f'Jogo {numJogo + 1}: {aposta}')
    sleep(0.5)
print(f'-=-=-=-=-=- BOA SORTE! -=-=-=-=-=-')