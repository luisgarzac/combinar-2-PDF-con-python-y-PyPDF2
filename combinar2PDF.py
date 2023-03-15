# Importamos PdfMerger de la librería PyPDF2
from PyPDF2 import PdfMerger

merger = PdfMerger() # Creamos el objeto del nuevo PDF
# Guardamos en "pdf" lo que contiene cada archivo dentro del []
for pdf in ["archivo1.pdf", "archivo2.pdf"]: 
    merger.append(pdf) # Utilizamos append() para unir el contenido que obtenga "pdf"

merger.write("archivo3_combinado.pdf") # creamos el nuevo archivo de PDF con el contenido de 2
merger.close()