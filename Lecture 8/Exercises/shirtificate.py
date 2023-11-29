from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.set_auto_page_break(auto=True, margin=15)
        
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(10) 

    def generate_certificate(self, nome):
        self.add_page(orientation='P', format='A4')
        self.image("./shirtificate.png", x=15, y=None, w=180)

        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", "", 24)
        self.set_xy(15, 60) 
        self.cell(180, 10, nome, align="C")


def main():
    pdf = PDF()
    pdf.generate_certificate(input("Name: "))
    pdf.output("shirtificate.pdf")
    
main()