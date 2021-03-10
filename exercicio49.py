opcao = 'S'
maiorcem = 0
totalgastos = 0
menorvalor = 9999999999999999999999999999999999999999999999999999999
produtomenor = ''
while opcao != 'N':
    if opcao == 'S':
        n = str(input('Nome do produto: '))
        valor = float(input('Valor R$: '))
        opcao = str(input('Deseja lançar outro produto [S/N]: ')).upper()
        totalgastos += valor
        if valor <= menorvalor:
            menorvalor = valor
            produtomenor = n
        if valor >= 100.0:
            maiorcem += 1
    else:
        print("Digite S para sim ou N para não!!!")
        n = str(input('Nome do produto: '))
        valor = float(input('Valor R$: '))
        opcao = str(input('Deseja lançar outro produto [S/N]: ')).upper()
print(f'Total dos gastos: {totalgastos:.2f}')
print(f'Quantos produtos custam mais que R$ 100,00: {maiorcem}')
print(f'Produto de menor valor: {produtomenor} que é R$ {menorvalor:.2f}')