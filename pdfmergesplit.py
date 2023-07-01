from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Merge two PDF files
def merge_pdfs():
    input_file1 = "C:\python\Practicum\pdfs\Harpreet Singh GTBIT 2023.pdf"
    input_file2 = "C:\python\Practicum\pdfs\Letterheadieee.pdf"
    output_file = "external.pdf"

    merger = PdfMerger()

    merger.append(input_file1)
    merger.append(input_file2)

    merger.write(output_file)

    merger.close()

    print("PDF files merged successfully!")

# Split into two
def split_pdf():
    input_file = r"C:\python\Practicum\pdfs\Java File till 19.pdf"
    output_file1 = "output1.pdf"
    output_file2 = "output2.pdf"
    split_page = int(input("Enter the page number from which you want to split: "))

    input_pdf = PdfReader(input_file)
    output_pdf1 = PdfWriter()
    output_pdf2 = PdfWriter()

    for page_num, page in enumerate(input_pdf.pages):
        if page_num < split_page:
            output_pdf1.add_page(page)
        else:
            output_pdf2.add_page(page)

    with open(output_file1, "wb") as f1:
        output_pdf1.write(f1)

    with open(output_file2, "wb") as f2:
        output_pdf2.write(f2)

    print("PDF file split successfully!")

#split_pdf()

merge_pdfs()

