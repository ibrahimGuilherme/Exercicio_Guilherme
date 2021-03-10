valor = float(input('Qual o valor: R$ '))
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
um = 0
while True:
    if valor - 50 >= 0:
        valor -= 50
        cinquenta += 1

    elif valor - 20 >= 0:
        valor -= 20
        vinte += 1
    elif valor - 10 >= 0:
        valor -= 10
        dez += 1
    elif valor - 5 >= 0:
        valor -= 5
        cinco += 1
    elif valor - 1 >= 0:
        valor -= 1
        um += 1
    else:
        break
if cinquenta >= 1:
    print(f'Total de {cinquenta} cédulas de R$ 50,00')
if vinte >= 1:
    print(f'Total de {vinte} cédulas de R$ 20,00')
if dez >= 1:
    print(f'Total de {dez} cédulas de R$ 10,00')
if cinco >= 1:
    print(f'Total de {cinco} cédulas de R$ 5,00')
if um >= 1:
    print(f'Total de {um} cédulas de R$ 1,00')