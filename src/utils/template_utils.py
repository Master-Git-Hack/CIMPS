from pptx.util import Pt
from pptx.dml.color import RGBColor
from src.config import temPath, public_pwd_for_file
from platform import system
from subprocess import call
from random import randrange as rg

def textStyle(insert, size = 10, isBold = False, fontName = 'Montserrat', color = RGBColor(0,0,0)):
    estilo = insert.font
    estilo.bold = isBold
    estilo.size = Pt(size)
    estilo.name = fontName
    estilo.color.rgb = color
    return insert

def pptx2pdf(filename, email):
    if system() == 'Linux':
        call(['libreoffice', '--headless', '--convert-to', 'pdf', f'./archivos/{filename}.pptx'])
    else:
        call(['soffice', '--headless', '--convert-to', 'pdf', f'./archivos/{filename}.pptx'])

    call(['mv', f'{temPath}{filename}.pdf', '{temPath}{filname}-tmp.pdf'])

    call(['pdftk', f'{temPath}{filename}-tmp.pdf', 'output', f'{temPath}{filename}.pdf', 'owner_pw', f'#{public_pwd_for_file}_{email}_{rg(10)}', '#url', 'allow', 'printing'])
    
    return True
