import PyPDF2
class Pdf_reader:
    #This function reads your pdf and converts it into a string
    def read_pdf(self, pdf_file):
        reader = PyPDF2.PdfReader(pdf_file)
        page_length = len(reader.pages)
        text = ""
        for item in range(0, int(page_length)):
            text += f"page {item + 1}"
            text += reader.pages[item].extract_text()
        return text