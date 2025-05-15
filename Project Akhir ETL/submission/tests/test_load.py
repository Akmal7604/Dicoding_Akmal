import pytest
import os
import pandas as pd
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

# Tambahkan root project ke path
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

from utils.load import (
    save_to_csv,
    save_to_google_sheets
)

def test_save_to_csv(tmp_path):
    """Menguji fungsi penyimpanan ke CSV"""
    # Buat sample DataFrame
    sample_df = pd.DataFrame({
        'title': ['Shirt 1', 'Shirt 2'],
        'price': [100000, 150000],
        'rating': [4.5, 4.2]
    })
    
    # Path file CSV sementara
    csv_path = tmp_path / 'test_products.csv'
    
    # Panggil fungsi
    with patch('builtins.print') as mock_print:
        save_to_csv(sample_df, str(csv_path))
        
        # Validasi
        assert os.path.exists(csv_path)
        
        # Baca kembali CSV untuk verifikasi
        loaded_df = pd.read_csv(csv_path)
        pd.testing.assert_frame_equal(sample_df, loaded_df)
        
        # Pastikan pesan berhasil dicetak
        mock_print.assert_called_once()

def test_save_to_google_sheets():
    """Menguji fungsi penyimpanan ke Google Sheets"""
    # Buat sample DataFrame
    sample_df = pd.DataFrame({
        'title': ['Shirt 1', 'Shirt 2'],
        'price': [100000, 150000],
        'rating': [4.5, 4.2]
    })
    
    # Mock Google Sheets dependencies
    with patch('gspread.authorize') as mock_authorize:
        # Buat mock client dan sheet
        mock_client = MagicMock()
        mock_sheet = MagicMock()
        mock_sheet.url = 'https://test-sheet-url'
        mock_client.create.return_value = mock_sheet
        
        # Mock credentials
        with patch('oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name') as mock_credentials:
            # Panggil fungsi dengan patch print
            with patch('builtins.print') as mock_print:
                save_to_google_sheets(sample_df, 'Test Worksheet')
                
                # Validasi
                mock_client.create.assert_called_once_with('Test Worksheet')
                mock_sheet.share.assert_called_once()
                mock_sheet.get_worksheet.assert_called_once_with(0)
                
                # Pastikan pesan berhasil dicetak
                assert mock_print.call_count == 2

def test_save_to_google_sheets_error():
    """Menguji error handling pada Google Sheets"""
    # Buat sample DataFrame
    sample_df = pd.DataFrame({
        'title': ['Shirt 1', 'Shirt 2'],
        'price': [100000, 150000],
        'rating': [4.5, 4.2]
    })
    
    # Mock Google Sheets dependencies
    with patch('gspread.authorize') as mock_authorize:
        # Simulasi exception
        mock_authorize.side_effect = Exception("Test Error")
        
        # Panggil fungsi dengan patch print
        with patch('builtins.print') as mock_print:
            save_to_google_sheets(sample_df, 'Test Worksheet')
            
            # Validasi
            mock_print.assert_called_once_with('Gagal menyimpan ke Google Sheets: Test Error')