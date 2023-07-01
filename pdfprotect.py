from PyPDF2 import PdfWriter, PdfReader
import getpass

pdf_writer = PdfWriter()
path = r"C:\python\Practicum\kuchbhi.pdf"
pdf = PdfReader(path)

for page_num in range(len(pdf.pages)):
    pdf_writer.add_page(pdf.pages[page_num])

password = getpass.getpass(prompt='ENTER Password: ')
pdf_writer.encrypt(password)

with open(path, "wb") as f:
    pdf_writer.write(f)
