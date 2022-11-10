"""File to handle extra utilities"""
from numpy import nan
from pandas import read_excel

# from .config import Config

# _schemas = Config().paths.schemas


def get_xlxs_data(
    filename: str,
    sheet_name: str = "Sheet 1",
    reference_col: str = "index",
    converters: dict = None,
    index_col: list = None,
) -> dict:
    """get info from xlsx file that contains the data to generate the certificates
    Args:
        filename (str): name of the file
        sheet_name (str): name of the sheet. Defaults to "Sheet 1".
        converters (dict): dict with the columns to convert to an specific data type. Defaults to None.
        index_col (list): list with the columns to use as index. Defaults to None.
    Returns:
        file (dict): dict with the data from the file
    """
    if converters is None:
        converters = {f"{reference_col}": int}
    if index_col is None:
        index_col = list([0])

    certificates = read_excel(
        f"./schemas/{filename}",
        sheet_name=sheet_name,
        converters=converters,
        index_col=index_col,
    )
    certificates = certificates.apply(
        lambda cell: cell.str.strip() if cell.dtype == "object" else cell
    )
    certificates["id_constancia"] = certificates.index
    # certificates.insert(loc=0, column='usuario',value='admin')
    return certificates.replace(r"^\s*$", nan, regex=True).to_dict(orient="records")


data = get_xlxs_data("commite.xlsx", "Hoja1", "Numero")
print(data)
