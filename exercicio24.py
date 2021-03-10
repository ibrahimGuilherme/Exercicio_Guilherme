velocidade = int(input('Qual a velocidade do seu carro em Km/h? '))
if velocidade > 80:
    multa = (velocidade-80)*5
    print(f'Você foi multado em R$ {multa}. Reduza a velocidade')
