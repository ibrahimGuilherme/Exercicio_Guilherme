from datetime import datetime
now = datetime.now()
maiores = 0
menores = 0
for num in range(1, 6):
    anoNas = int(input('Ano de nascimento: '))
    if anoNas - now.year >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Maiores = {maiores}')
print(f'Menores = {menores}')