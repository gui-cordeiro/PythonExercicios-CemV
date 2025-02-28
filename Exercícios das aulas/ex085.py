# Exercício 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#                que mantenha separados os valores pares e ímpares (duas listas separadas dentro de uma única lista).
#                No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]
valor = 0

for cont in range(0,7):
    valor = int(input(f'Digite o {cont + 1}o. valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f'a) Valores pares digitados: {numeros[0]}')
print(f'b) Valores ímpares digitados: {numeros[1]}')