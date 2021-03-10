maior = 0
menor = 9999999999999999999999999999999999999999

for num in range(0, 5):
    peso = int(input('Digite seu peso: '))
    if peso >= maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'Maior peso: {maior}Kg')
print(f'Menor peso {menor} Kg')