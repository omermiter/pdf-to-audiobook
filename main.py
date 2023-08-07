from reader import Pdf_reader
from audio_transform import To_audio


pdf = "sample.pdf"
reader = Pdf_reader()
pdf_text = reader.read_pdf(pdf)
converter = To_audio()
converter.transform(pdf_text)
converter.play()



