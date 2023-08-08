from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo: ")

valor_total = int(horas_previstas) * int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
# pdf.image("template.png", x = 0, y = 0)

pdf.text(10, 10, "Semana do Python na prática | Empowerdata")
pdf.text(110, 140, projeto)
pdf.text(110, 150, horas_previstas)
pdf.text(110, 160, valor_hora)
pdf.text(110, 170, prazo)
pdf.text(110, 180, str(valor_total))

pdf.output("./aula_1/Orçamento.pdf")
print("Orçamento gerado com sucesso.")