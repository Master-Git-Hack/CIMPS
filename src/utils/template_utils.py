from pptx.util import Pt
from pptx.dml.color import RGBColor
from src.config import temPath, public_pwd_for_file
from os import uname
from subprocess import call
from pandas import read_excel, isna
from numpy import nan
from random import randrange as rg


# function to read excel file
def getXLSXinfo():
    certificates = read_excel(open('src/schemas/Becas.xlsx', 'rb'), sheet_name = 'Sheet 1', converters = {'idx:int'}, index_col = [0])
    return certificates.replace(r'^\s*$', nan, regex = True)

#function to set style for pptx
def textStyle(insert, size = 10, isBold = False, fontName = 'Montserrat', color = RGBColor(0,0,0), alignment_center = False):
    estilo = insert.font
    estilo.bold = isBold
    estilo.size = Pt(size)
    estilo.name = fontName
    estilo.color.rgb = color
    return insert

def elements2change(nombre = 'John Doe', puesto = 'Asistente', lugar = False, title = False, year = 21):
    #every index represent a value to change, example: at index 2 it changes name value at certificate
    return {
        'paragraphs' : {
            2 : f'{nombre.upper()}',
            3 : '',
            4 : f'{title.upper() if title != False else puesto.upper() }',
        },
        'font' :  'Calibri',
        'color' : RGBColor(136,0,0),
        'bold' : True,
        'size' : 32 if len(nombre) <= 30 else 24,
        'isFragmented' : {
            2 : False,
            3 : True,
            4 : False
        },
        'text_fragmented':{
            3:{
                'paragraphs':{
                    1 : 'Por su valiosa participación ' + ('' if title == False else 'como:'), 
                    2 : f' {puesto.upper()} ' if title != False else '',
                    3 : f'en el Congreso Internacional CIMPS 20{year} ' if title == False else '',
                    4 : f'{"en el " if lugar != False else "como: "}',
                    5 : f'{lugar if lugar != False else ""}' 
                },
                'font' : 'Calibri',
                'bold': {
                    1 : False,
                    2 : True,
                    3 : False,
                    4 : False,
                    5 : True
                },
                'size' : 16,
                'color' : RGBColor(0,0,0)
            }
        }
    }

# function to transform pptx to pdf and encrypt it
def pptx2pdf(filename, email):
    action = False
    certificate = f'{temPath}{filename}'
    match uname().sysname:
        case 'Linux':
            call(['libreoffice', '--headless', '--invisible', '--convert-to', 'pdf:writer_pdf_Export', '--outdir', f'{temPath}', f'{certificate}.pptx'])
            action = True
        case 'Darwin':
            call(['soffice', '--headless', '--invisible', '--convert-to', 'pdf:writer_pdf_Export', '--outdir', f'{temPath}', f'{certificate}.pptx'])
            action = True
        case 'Windows':
            print('case not implemented')
        case _:
            print('OS name not detected or supported')

    if action:
        #call(['mv', f'{certificate}.pdf', f'{certificate}-tmp.pdf'])

        #call(['rm', f'{certificate}.pptx'])

        #call(['pdftk', f'{certificate}-tmp.pdf', 'cat', 'output', f'{certificate}.pdf', 'owner_pw', f'#{public_pwd_for_file}_{email}_{rg(10)}', 'allow', 'printing'])

        #call(['rm', f'{certificate}-tmp.pdf'])
        
        return True
    else:
        return False


def protect_pdf(certificate,email):

    call(['mv', f'{certificate}.pdf', f'{certificate}-tmp.pdf'])
    
    call(['pdftk', f'{certificate}-tmp.pdf', 'cat', 'output', f'{certificate}.pdf', 'owner_pw', f'#{public_pwd_for_file}_{email}_{rg(10)}', 'allow', 'printing'])

    call(['rm', f'{certificate}-tmp.pdf'])

    call(['rm', f'{certificate}.pptx'])
    return True

def end_process(filename):
    certificate = f'{temPath}{filename}'
    call(['rm', f'{certificate}.pdf'])
    return True
