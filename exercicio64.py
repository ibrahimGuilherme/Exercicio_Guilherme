def media(n1=10, n2=4):
    med = (n1 + n2)/2
    print(f'A média de {n1} e {n2} é {med:.2f}\n')
media()

def meuNome(n='Ibrahim Guilherme Moraes de Oliveira'):
    print(n + '\n')
meuNome()

def exibiNome(n3='Ibrahim Guilherme', n4='Moraes de Oliveira'):
    print(f'Nome completo: {n3} {n4}\n')
exibiNome()

def inverso(nome='Paralelepípedo'):
    inverter= nome[::-1]
    print(f'{nome} --> {inverter}\n')
inverso()