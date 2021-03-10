salario = float(input('\033[31mValor atual do salário: R$ \033[m'))
if salario <= 1500.00:
    valor = salario * 1.2
    print(f'Novo salário: \033[34mR$ {valor:.2f}')
else:
    valor = salario * 1.1
    print(f'Novo salário: \033[34mR$ {valor:.2f}')