nomes = 'a'
lista = []
n = 0
while nomes != '':
    nomes = str(input('Digite um nome: '))
    lista += [nomes]
del(lista[-1])
lista.sort()
print('Nomes Ordenados:')
print(lista)
for item in lista:
    print(f'{n}. {item}')
    n += 1
excluir = int(input('Qual item você deseja excluir, digite o índice: '))
del(lista[excluir])
print(lista)
