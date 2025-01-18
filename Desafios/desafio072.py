numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
           "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 0 and num < 20:
        print(f'Você escolheu o número \'{numeros[num]}\'.')
        break
    else:
        print('Tente novamente. ', end='')