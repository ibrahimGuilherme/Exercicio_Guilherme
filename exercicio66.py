def calculadora():
    print('\n' + '-' * 40)
    print(f'{"         AGENDA DE CONTATOS"}')
    print('-' * 40)
def menu():
    calculadora()
    print('1. Listar contatos')
    print('2. Exibir informações de um contato')
    print('3. Incluir um contato')
    print('4. Apagar um contato')
    print('5. Sair')
nome1 = 'Guilherme'
numero1 = '897789877'
nome2 = 'Fábio'
numero2 = '097284373'

con = 0

l1 = [nome1, nome2]
l2 = [numero1, numero2]

while True:
    menu()
    opcao = int(input('Qual a sua opção [1/2/3/4/5]? '))

    if opcao < 1 or opcao > 5:
        print('\nOpção inválida')
        input('\nPressione <ENTER>\n')
        continue
    elif opcao == 2:
        i = input('Digite o código do contato: ')
        if i == '1':
            print('Código: 1')
            print(f'nome: {l1[0]}')
            print(f'Telefone: {l2[0]}')
        elif i == '2':
            print('Código: 2')
            print(f'nome: {l1[1]}')
            print(f'Telefone: {l2[1]}')
        input('\nPressione <ENTER>\n')
    elif opcao == 3:
        n = []
        a = int(input('Código: '))
        b = input(f'nome: ')
        c = int(input(f'Telefone: '))
        n.append(a)
        n.append(b)
        n.append(c)
        print('contato incluído!')
        input('\nPressione <ENTER>\n')
    if opcao == 1:
        print('\n' + '-' * 40)
        print(f'{"         AGENDA DE CONTATOS"}')
        print('-' * 40)
        print('Cod nome                    Telefone')
        print(f'1 {nome1}                    {numero1}')
        print(f'2 {nome2}                    {numero2}')
        try:
            print(f"{n[1]}                        {n[2]}")
        except NameError:
            input('\nPressione <ENTER>\n')
    elif opcao == 4:
        y = input('Digite o código que será apagado: ')
        if y == 1:
            del(l1[0])
            del(12[0])
        elif y == 2:
            del(l1[1])
            del(12[1])
        elif y == 3:
            del(n[0])
            del(n[1])
            del(n[2])
        input('\nPressione <ENTER>\n')
    elif opcao == 5:
        break
    con += 1