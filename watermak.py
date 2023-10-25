#Cara Pake, python watermak.py "Teks yang mau ditambahkan di dokumen pdf" L filepdfyangmodikasihwatermark.pdf filedaftarorangyangrequest.txt
# L untuk landscape, karakter lain bebas buat apa saja,
# filedaftarorangyangrequest.txt bebas yang penting file teks berisi requester per baris per orang.

#Requirements : pypdf, reportlab
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from pypdf import PdfReader, PdfWriter

#text = input("Masukkan Teks untuk watermark : ")
#filesumber = input("Masukkan nama file pdf sumber : ")
#peataul = input("ini landscape atau Portrait ? ")
#listrequester = input("Masukkan file requester document ")
try:
    text = sys.argv[1]
except:
    text = "Dokumen terbatas dan rahasia, requested by "
    
def makeWatermark(caimark):
    if sys.argv[2]=="L":
        coco = 0
        pdf = canvas.Canvas("watermark.pdf", pagesize=landscape(A4))
        pdf.rotate(35) #sudut kemiringan teks watermark nanti jika pilih landscape 
    else:
        coco = 1
        pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
        pdf.rotate(55) #sudut kemiringan teks watermark nanti jika pilih non landscape
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.red, alpha=0.6) #warna teks watermark
    pdf.setFont("Helvetica", 20)    #font dan ukuran font watermark
    pdf.drawCentredString(pdf._pagesize[coco]/2, 0, f'{text} {caimark}')
    pdf.save()

def makepdf(asup):
    pdf_file = sys.argv[3]
    watermark = 'watermark.pdf'
    merged = f"{pdf_file.replace('.pdf','')}_{asup}.pdf"

    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]
        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)
		
data = open(sys.argv[4],'r').read().splitlines()
for ngaran in data:
	makeWatermark(ngaran)
	makepdf(ngaran)