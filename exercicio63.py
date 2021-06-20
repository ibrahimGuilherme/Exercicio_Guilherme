apartamentos = {}
while True:
    n2 = str(input('Nome: '))
    n1 = str(input('Telefone: '))

    if n1 == '' and n2 =='':
        break
    apartamentos[int(n1)] = n2
print(apartamentos)

print('\nAgenda de Telefones\n-------------------')

for chave, valor in apartamentos.items():
    print(f'Nome: {valor} - Telefone: {chave}')