contParentesis = 0

frase = input("Digite a seguir um texto qualquer: ")

for caracter in frase:
    if caracter == '(':
        contParentesis += 1
    elif caracter == ')':
        contParentesis -= 1

if contParentesis == 0:
    print("Não há parêntesis em aberto, parabéns!")
elif contParentesis > 0:
    print(f"Você se esqueceu de fechar {contParentesis} parêntesis.")
else:
    if contParentesis == -1:
        print(f"Há {abs(contParentesis)} fechamento de parêntesis extra.")
    else:
        print(f"Há {abs(contParentesis)} fechamentos de parêntesis extras.")