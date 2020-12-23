import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', 
                                                         scope)
client = gspread.authorize(creds)

sheet = client.open("Global Music").sheet1



def insert_data(data):

    """Fills spreadsheet with data from dictionaries.

    Args:
        data (dict): Dictionary containing album details.
    """

    offset = len(sheet.col_values(1))

    cell_list = sheet.range(f'A{offset+1}:F{offset+1}')
    
    try:
        if (data['album_title'] not in sheet.col_values(2)):
            print("Adding " + data['album_title'])
            for cell, value in zip(cell_list, data.values()):
                cell.value = value
            sheet.update_cells(cell_list)
    except:
        print("Problem inserting data for:", data)

