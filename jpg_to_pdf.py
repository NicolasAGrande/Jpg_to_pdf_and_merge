import PyPDF2
from PyPDF2 import PdfFileMerger
from PIL import Image

img1 = Image.open(input(r''))
img2 = Image.open(input(r''))

im1 = img1.convert('RGB')
im1.save(r'img1.pdf')
im2 = img2.convert('RGB')
im2.save(r'img2.pdf')

arqui1 = open('img1.pdf','rb')
arqui2 = open('img2.pdf','rb')
dadosImg1 = PyPDF2.PdfFileReader(arqui1)
dadosImg2 = PyPDF2.PdfFileReader(arqui2)

merge = PyPDF2.PdfFileMerger()

merge.append(dadosImg1)
merge.append(dadosImg2)

merge.write(r"Merge.pdf")