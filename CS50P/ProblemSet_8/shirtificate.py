from fpdf import FPDF

pdf = FPDF()

name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")

pdf.add_page()

#for the text outside the shirt
pdf.set_font('helvetica', "B", size=50)
pdf.cell(0, 40, text="CS50 Shirtificate", align = 'C')
pdf.image("shirtificate.png", x=5, y=50, w= 200, h= 220)

#for the text inside the shirt
pdf.set_font('helvetica', size=30)
pdf.set_text_color(255,255,255)
pdf.text(50 ,130 ,f"{name} took CS50")

pdf.output("shirtificate.pdf")