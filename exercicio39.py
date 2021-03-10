soma = 0
for num in range(0, 6):
    n = int(input(f'Número {num + 1}: '))
    if n%2 == 0:
        soma += n
    else:
        continue
print(f'Soma dos números pares = {soma}')