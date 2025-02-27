from random import randint

num = ((randint(0,10)), (randint(0,10)), (randint(0,10)), (randint(0,10)), (randint(0,10)))

print(num)
maior = 0;
menor = num[0];

for cont in range(0, len(num)):
    if maior < num[cont]:
        maior = num[cont]
    if menor > num[cont]:
        menor = num[cont]

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')