from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

while True:
    carros = input(str('Digite o nome de um carro: '))
    if carros != '':
        carros = input(str('Digite o nome de um carro: '))
        convidados = [[carros]]
        convidados.append([carros])
    else:
        break
convidados = convidados
pdf.set_font('courier', '', 12)
cont = 0
for convidado in convidados:
    carro = convidado[cont]
    cont += 1
    pdf.cell(0, 10, f'{carro:<35}     ', 0, 1, 'C')


pdf.output('carros.pdf', 'F')