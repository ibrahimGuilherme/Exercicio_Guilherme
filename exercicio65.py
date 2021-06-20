def menu():
    print('Cód. Carro                         Valor')
    print('-' * 48)
    print('1    HB20 1.0 Comfort Plus           R$ 33590.00')
    print('2    200B Allure 1.6 16V             R$ 71990.00')
    print('3    Argo Drive 1.0 Firefly          R$ 44900.00')
    print('4    Corolla Sedan SEG 1.8 16V       R$ 44900.00')
    print('5    KA 1.0 SE                       R$ 34900.00')
    print('6    Fox 1.0 VHT                     R$ 26990.00')
    print('0    Sair do programa\n')



while True:
    menu()
    opcao = int(input('Código do carro: '))

    if opcao < 0 or opcao > 6:
        print('\nOpção inválida')
        continue
    if opcao == 1:
        print('\nnValor de venda do carro HB20 1.0 Comfort Plus é R$ 33590.00\n')
    elif opcao == 2:
        print('\nValor de venda do carro 200B Allure 1.6 16V é R$ 71990.00\n')
    elif opcao == 3:
        print('\nValor de venda do carro Argo Drive 1.0 Firefly é R$ 44900.00\n')
    elif opcao == 4:
        print('\nValor de venda do carro Corolla Sedan SEG 1.8 16V é R$ 44900.00\n')
    elif opcao == 5:
        print('\nValor de venda do carro KA 1.0 SE é R$ 34900.00\n')
    elif opcao == 6:
        print('\nValor de venda do carro Fox 1.0 VHT é R$ 26990.00\n')
    elif opcao == 0:
        break