d1 = {1:'Valor R$ 28000.00', 2:'Gol', 3:'Valor R$ 21250.00', 4:'Corsa'}
c = None
while c != '':
    c = str(input('Qual o carro procurado? '))
    if c == 'Gol':
        print(f'{d1[2]} - {d1[1]}')
    elif c == 'Corsa':
        print(f'{d1[4]} - {d1[3]}')
    else:
        print('A loja não possui esse carro.')