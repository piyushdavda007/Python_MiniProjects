# import useful modules

from PyPDF2 import PdfFileWriter, PdfFileReader

# merge pdfs together.
# step->
# open your first pdf
# open your second pdf
# for each page, copy it to third pdf
# open a third pdf
write_obj = PdfFileWriter()
pdf_list = ["Playing with PDFs\\Resume1.pdf",
            "Playing with PDFs\\Resume2.pdf"]


for i in pdf_list:
    red_obj = PdfFileReader(i)
    pages = red_obj.getNumPages()
    # print(pages)
    for j in range(pages):
        p = red_obj.getPage(j)
        write_obj.addPage(p)


pdf_file = open(
    "Playing with PDFs\\merged.pdf", 'wb')
write_obj.write(pdf_file)


# encrypt a pdf
write_obj = PdfFileWriter()
write_obj.encrypt('password', 'owner_password', True)


pdf_file = open(
    "Playing with PDFs\\merged.pdf", 'wb')
write_obj.write(pdf_file)


# add watermark to a pdf
# steps->
# read the pdf
# read the watermark
# create a new pdf
# for each page in pdf, merge watermark with it and
# add it to the new pdf.

pdf = PdfFileReader(
    "Playing with PDFs\\Resume1.pdf")
watermark = PdfFileReader(
    "Playing with PDFs\\watermark.pdf")
page_w = watermark.getPage(0)
new_pdf = PdfFileWriter()
pages = pdf.getNumPages()
for i in range(pages):
    page = pdf.getPage(i)
    page.mergePage(page_w)
    new_pdf.addPage(page)

pdf_fl = open(
    "Playing with PDFs\\pdf+watermark.pdf", 'wb')
new_pdf.write(pdf_fl)

pdf_fl.close()
