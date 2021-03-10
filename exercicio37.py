soma = 0
for num in range(0, 501, 3):
    if num%2 == 0:
        continue
    else:
        print(num)
        soma += num
print('Soma =', soma)
