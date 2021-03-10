nome = input('Cidade: ').upper()
spli = nome.split()
n2 = spli[0]
if n2 == 'SÃO':
    situacao = 'true'
else:
    situacao = 'false'
print(situacao)