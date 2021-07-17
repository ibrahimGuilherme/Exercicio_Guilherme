from fpdf import FPDF
pdf = FPDF('P', 'pt', 'A3')

pdf.add_page()

pdf.set_font('Arial','', 12)
pdf.cell(0, 20, 'Vermelho', 0, 1, 'L')

pdf.set_font('Times','', 6)
pdf.cell(0, 20, 'Verde', 0, 1, 'L')

pdf.set_font('Arial','B', 16)
pdf.cell(0, 20, 'Amarelo', 0, 1, 'L')

pdf.set_font('Times','B', 4)
pdf.cell(0, 20, 'Preto', 0, 1, 'L')

pdf.set_font('Arial','I', 12)
pdf.cell(0, 20, 'Branco', 0, 1, 'L')

pdf.set_font('Times','I', 12)
pdf.cell(0, 20, 'Azul', 0, 1, 'L')

pdf.output('vinte_mil_leguas.pdf', 'F')