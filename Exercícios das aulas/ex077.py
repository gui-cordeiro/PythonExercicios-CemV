palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for cont in range(0, len(palavras)):
    print(f'Na palavra {palavras[cont].upper()} temos ', end='')
    for vowel in palavras[cont]:
        if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
            print(f'{vowel} ', end='')
    print('')