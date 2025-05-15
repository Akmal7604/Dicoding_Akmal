import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_to_csv(df, filename='products.csv'):
    """Simpan DataFrame ke CSV"""
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke {filename}")

def save_to_google_sheets(df, worksheet_name='Fashion Studio Products'):
    """
    Simpan DataFrame ke Google Sheets
    
    Prasyarat: 
    - Miliki google-sheets-api.json
    - Install oauth2client dan gspread
    """
    try:
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            't-osprey-423904-j0-e68778716ba7.json', scope
        )
        
        client = gspread.authorize(credentials)
        sheet = client.create(worksheet_name)
        sheet.share(None, perm_type='anyone', role='writer')
        
        worksheet = sheet.get_worksheet(0)
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        
        print(f"Data berhasil disimpan ke Google Sheets: {worksheet_name}")
        print(f"Spreadsheet berhasil dibuat. Cek di Google Sheets: {sheet.url}")
    
    except Exception as e:
        print(f"Gagal menyimpan ke Google Sheets: {e}")