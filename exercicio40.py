n = int(input('Digite um número: '))
print('Os divisores irão aparecer.')
soma = 0
for num in range(1, n +1):
    if n%num == 0:
        print(num, end=' ')
        soma = soma + 1

if soma > 2:
    print(f'\nO número {n} possui {soma} divisores, então ele não é PRIMO')
else:
    print(f'\nO número {n} possui {soma} divisores, então ele é PRIMO')