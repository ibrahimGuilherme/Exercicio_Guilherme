n1 = None
lista = [n1]
cont = 0
t = 0
while n1 != '':
    n1 = input('Digite um número: ')
    lista.append(n1)
del(lista[0])
del(lista[-1])
print(lista)
for item in lista:
    t += 1
t = t//2
print(lista[:t])
while cont < len(lista):
    print(int(lista[cont])*50)
    cont += 1
