from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
#P stands for Portrait => taller than it is wide
#"mm": the unit of measure : millimeters
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page() #first master page
    pdf.set_font(family="Times", style="B", size=24) #to specify the text properties
    pdf.set_text_color(100, 100, 100) # grey color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) # this line adds a cell to contain atext
    pdf.line(x1=10, y1=20, x2=200, y2=20)


    #Setting the footer:
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")#alignement right


    for i in range(row["Pages"] - 1):
        pdf.add_page() # second:  pages
        #Setting the footer:
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")


