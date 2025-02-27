lista = []
opt = 'S'

while opt == 'S' or opt == 's':
    num = int(input(f"Digite um número para ocupar a {len(lista) + 1}o posição da lista: "))
    lista.append(num)
    opt = input("Deseja inserir um outro número? [S/N]: ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"Sua lista é: {lista}\n")

print(f"A) A sua lista tem {len(lista)} elementos;")
lista.sort(reverse=True)
print(f"B) Sua lista ordenada de trás pra frente: {lista};")
print(f"C) O número 5 aparece {lista.count(5)} ", end='')
if lista.count(5) == 1:
    print("vez na lista.")
else:
    print("vezes na lista.")