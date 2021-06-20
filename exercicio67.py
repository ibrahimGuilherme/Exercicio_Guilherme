arq = open('cores.txt', 'r')
arq1 = open('cores1.txt', 'r')

print('Exibindo com um laço FOR\n', '-'*24)
for cores in arq:
    print(cores)

print('Exibindo com um laço WHILE\n', '-'*24)

linha = arq1.read()
cont = 1
while len(linha) > 0:

    print(linha)
    cont += 1
    if cont == 2:
        break

arq.close()
arq1.close()