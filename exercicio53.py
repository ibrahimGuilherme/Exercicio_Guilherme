l1 = None
l2 = None
lista = [[l1], [l2]]
while True:
    l1 = input('Nome: ')
    l2 = input('idade: ')
    lista[0].append(l1)
    lista[1].append(l2)
    if lista[0][-1] == '' and lista[1][-1] == '':
        del(lista[0][-1])
        del(lista[1][-1])
        del(lista[0][0])
        del(lista[1][0])
        break
t = 0
for item in lista[0]:
    if t > len(lista[1]):
        break
    print(item, '-', lista[1][t])
    t += 1
print(f'O primeiro nome {lista[0][0]}')
print(f'O último nome {lista[0][-1]}')