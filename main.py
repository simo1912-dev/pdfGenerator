from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
#P stands for Portrait => taller than it is wide
#"mm": the unit of measure : millimeters
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24) #to specify the text properties
    pdf.set_text_color(100, 100, 100) # grey color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1) # this line adds a cell to contain atext
    pdf.line(x1=10, y1=20, x2=200, y2=20)

pdf.output("output.pdf")


