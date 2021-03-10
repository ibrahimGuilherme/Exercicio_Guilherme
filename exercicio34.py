valor = float(input('Qual o valor normal do livro R$ '))
print('Formas de pagamento: \n'
      '1 - A vista com dinheiro \n'
      '2 - A vista com cartão \n'
      '3 - Em 2 vezes no cartão \n'
      '4 - 3 ou mais vezes no cartão')
formaPag = int(input('Qual a sua forma de pagamento: '))
if formaPag == 1:
    print(f'Valor que deve ser pago R$ {valor*0.9:.2f}')
elif formaPag == 2:
    print(f'Valor que deve ser pago R$ {valor * 0.95:.2f}')
elif formaPag == 3:
    print(f'Valor que deve ser pago R$ {valor:.2f}')
elif formaPag == 4:
    print(f'Valor que deve ser pago R$ {valor * 1.2:.2f}')