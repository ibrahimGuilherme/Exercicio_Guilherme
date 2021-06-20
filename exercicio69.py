arq = open('carros.txt', 'a')

carros = str(input('Digite um carro: '))
while len(carros) > 0:
    n = arq.writelines(f'{carros.strip("")}\n')
    carros = str(input('Digite um carro: '))

arq.close()
arq = open('carros.txt', 'r')

print('\nLendo o arquivo e exibindo na tela\n----------------------------------')
for x in arq:
    print(x)

arq.close()