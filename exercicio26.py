km = int(input('Qual a distância da viagem em Km? '))
if km <= 100:
    valor = km*0.60
    print(f'\033[31mValor da passagem: {valor:.2f}')
else:
    valor = km*0.50
    print(f'Valor da passagem: {valor:.2f}')