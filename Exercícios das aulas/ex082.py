listaMestre = []
listaPar = []
listaImpar = []
opt = 'S'

while opt == 'S' or opt == 's':
    num = int(input(f"Digite um número para ocupar a {len(listaMestre) + 1}o posição da lista: "))
    listaMestre.append(num)
    opt = input("Deseja inserir um outro número? [S/N]: ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

for num in listaMestre:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f"Lista completa: {listaMestre} | Tamanho: {len(listaMestre)};")
print(f"Lista com os números pares: {listaPar};")
print(f"Lista com os números ímpares: {listaImpar}.")