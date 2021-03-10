imovel = float(input('Valor do imóvel: R$ '))
salario = float(input('Valor do seu salário: R$ '))
anos = int(input('Em quantos anos será realizado o pagamento: R$ '))
prestacaoMaxima = salario*0.30
prestacao = imovel/(anos*12)
if prestacao < prestacaoMaxima:
    print(f'Parabéns! Empréstimo aprovado com a prestação de {prestacao:.2f}')
else:
    print(f'Desculpe, mas não podemos aprovar o seu empréstimo.\n'
          f'O valor de {prestacao:.2f} é maior do que podemos aprovar de acordo com seu salário, que é de {prestacaoMaxima:.2f}')