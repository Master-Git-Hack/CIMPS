from math import ceil
from os import uname
from random import randrange as rg
from subprocess import call

from numpy import nan
from pandas import isna, read_excel
from pptx.dml.color import RGBColor
from pptx.util import Pt

from src.config import public_pwd_for_file, temPath


# function to read excel file
def getXLSXinfo():
    certificates = read_excel(
        open("src/schemas/cientifico2022.xlsx", "rb"),
        sheet_name="Hoja1",
        converters={"Numero": str},
        index_col=[0],
    )
    return certificates.replace(r"^\s*$", nan, regex=True)


# function to set style for pptx
def textStyle(
    insert,
    size=10,
    isBold=False,
    fontName="Montserrat",
    color=RGBColor(0, 0, 0),
    alignment_center=False,
):
    estilo = insert.font
    estilo.bold = isBold
    estilo.size = Pt(size)
    estilo.name = fontName
    estilo.color.rgb = color
    return insert


def elements2change(
    nombre="John Doe", puesto="Asistente", lugar=False, title=False, year=21
):
    # every index represent a value to change, example: at index 2 it changes name value at certificate
    if isinstance(title, str):
        title = title.split(" ")
    new_title = ""
    for idx, word in enumerate(title or "ASISTENTE"):
        if idx == ceil(len(title or "ASISTENTE") / 2):
            new_title += f"\n"
        else:
            new_title += f"{word} "
    title = new_title.split(".")[0]
    return {
        "paragraphs": {
            2: f"{nombre.upper()}",
            3: "",
            4: f"{title.upper()}",
        },
        "font": "Calibri",
        "color": RGBColor(136, 0, 0),
        "bold": True,
        "size": 26,
        "isFragmented": {2: False, 3: True, 4: False},
        "text_fragmented": {
            3: {
                "paragraphs": {
                    1: "Por su valiosa participación como: ",
                    2: f"Asistente",
                    3: f" en el Congreso Internacional\n CIMPS 20{year} ",
                    4: "en el ",
                    5: f"{lugar}:\n",
                },
                "font": "Calibri",
                "bold": {1: False, 2: True, 3: False, 4: False, 5: True},
                "size": 16,
                "color": RGBColor(0, 0, 0),
            }
        },
    }


# function to transform pptx to pdf and encrypt it
def pptx2pdf(filename, email):
    action = False
    certificate = f"{temPath}{filename}"
    match uname().sysname:
        case "Linux":
            call(
                [
                    "libreoffice",
                    "--headless",
                    "--invisible",
                    "--convert-to",
                    "pdf:writer_pdf_Export",
                    "--outdir",
                    f"{temPath}",
                    f"{certificate}.pptx",
                ]
            )
            action = True
        case "Darwin":
            call(
                [
                    "soffice",
                    "--headless",
                    "--invisible",
                    "--convert-to",
                    "pdf:writer_pdf_Export",
                    "--outdir",
                    f"{temPath}",
                    f"{certificate}.pptx",
                ]
            )
            action = True
        case "Windows":
            print("case not implemented")
        case _:
            print("OS name not detected or supported")

    if action:
        # call(['mv', f'{certificate}.pdf', f'{certificate}-tmp.pdf'])

        # call(['rm', f'{certificate}.pptx'])

        # call(['pdftk', f'{certificate}-tmp.pdf', 'cat', 'output', f'{certificate}.pdf', 'owner_pw', f'#{public_pwd_for_file}_{email}_{rg(10)}', 'allow', 'printing'])

        # call(['rm', f'{certificate}-tmp.pdf'])

        return True
    else:
        return False


def protect_pdf(certificate, email):

    call(["mv", f"{certificate}.pdf", f"{certificate}-tmp.pdf"])

    call(
        [
            "pdftk",
            f"{certificate}-tmp.pdf",
            "cat",
            "output",
            f"{certificate}.pdf",
            "owner_pw",
            f"#{public_pwd_for_file}_{email}_{rg(10)}",
            "allow",
            "printing",
        ]
    )

    call(["rm", f"{certificate}-tmp.pdf"])

    call(["rm", f"{certificate}.pptx"])
    return True


def end_process(filename):
    certificate = f"{temPath}{filename}"
    call(["rm", f"{certificate}.pdf"])
    return True
