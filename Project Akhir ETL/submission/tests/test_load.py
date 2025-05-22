import pytest
import os
import pandas as pd
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Tambahkan root project ke path
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

from utils.load import save_to_csv, save_to_google_sheets

def test_save_to_csv(tmp_path):
    """Menguji fungsi penyimpanan ke CSV"""
    sample_df = pd.DataFrame({
        'title': ['Shirt 1', 'Shirt 2'],
        'price': [100000, 150000],
        'rating': [4.5, 4.2]
    })

    csv_path = tmp_path / 'test_products.csv'

    with patch('builtins.print') as mock_print:
        save_to_csv(sample_df, str(csv_path))

        assert os.path.exists(csv_path)

        loaded_df = pd.read_csv(csv_path)
        pd.testing.assert_frame_equal(sample_df, loaded_df)

        mock_print.assert_called_once()

@patch('gspread.authorize')
@patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name')
def test_save_to_google_sheets(mock_credentials, mock_authorize):
    """Menguji fungsi penyimpanan ke Google Sheets"""
    sample_df = pd.DataFrame({
        'title': ['Shirt 1', 'Shirt 2'],
        'price': [100000, 150000],
        'rating': [4.5, 4.2]
    })

    mock_client = MagicMock()
    mock_sheet = MagicMock()
    mock_sheet.url = 'https://test-sheet-url'

    # Pastikan mock_client digunakan dalam otorisasi
    mock_authorize.return_value = mock_client

    # Mock open agar selalu memicu SpreadsheetNotFound
    mock_client.open.side_effect = gspread.SpreadsheetNotFound
    mock_client.create.return_value = mock_sheet

    with patch('builtins.print') as mock_print:
        save_to_google_sheets(sample_df, 'Test Worksheet')

        mock_client.create.assert_called_once_with('Test Worksheet')
        mock_sheet.share.assert_called_once()
        mock_sheet.get_worksheet.assert_called_once_with(0)

        assert mock_print.call_count == 2

