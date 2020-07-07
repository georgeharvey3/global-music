import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', 
                                                         scope)
client = gspread.authorize(creds)

sheet = client.open("Global Music").sheet1

offset = len(sheet.col_values(1))


def insert_data(data_list):

    """Fills spreadsheet with data from dictionaries.

    Args:
        data_list (list): List of dictionaries containing album details.
    """

    for i, data in enumerate(data_list):
        cell_list = sheet.range(f'A{i+offset+1}:F{i+offset+1}')
        for cell, value in zip(cell_list, data.values()):
            cell.value = value
        sheet.update_cells(cell_list)

