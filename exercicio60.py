apartamentos = {}
while True:
    n1 = str(input('Número do apartamento: '))
    n2 = str(input('Nome do proprietário: '))

    if n1 == '' and n2 =='':
        break
    apartamentos[int(n1)] = n2
print('\nDicionário:')
print(apartamentos)

for chave, valor in apartamentos.items():
    print(f'Número: {chave} - Proprietário: {valor}')