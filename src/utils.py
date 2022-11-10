"""File to handle extra utilities"""
from numpy import nan
from pandas import read_excel

from .config import Config

_tmp = Config().paths.temp


def get_xlxs_info(filename: str, sheet_name: str) -> read_excel:
    """get info from xlsx file that contains the data to generate the certificates
    Args:
        filename (str): name of the file
        sheet_name (str): name of the sheet
    Returns:
        read_excel: pandas object
    """
    certificates = read_excel(
        f"{_tmp}/{filename}",
        sheet_name=sheet_name,
        converters={"idx:int"},
        index_col=[0],
    )
    return certificates.replace(r"^\s*$", nan, regex=True)
