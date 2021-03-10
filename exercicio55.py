lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
lista.append(30)
lista.insert(0, 20)
lista.insert(2, 10000)
print(lista)
lista[3] = 'Python'
del(lista[4])
print(lista)
print(lista.pop(-1))
print(lista)