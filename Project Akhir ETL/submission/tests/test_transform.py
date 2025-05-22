# tests/test_transform.py
import pytest
import pandas as pd
import numpy as np

import sys
from pathlib import Path

# Tambahkan root project ke path
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

from utils.transform import (
    clean_price,
    clean_rating,
    transform_data
)

def test_clean_price():
    """Menguji fungsi pembersihan harga"""
    # Test berbagai format harga
    assert clean_price('Rp 100.000') == 1600000  # 100.000 * 16000
    assert clean_price('$430.75') == 6892000  # 50 * 16000
    assert clean_price('Invalid') is None

def test_clean_rating():
    """Menguji fungsi pembersihan rating"""
    assert clean_rating('Rating: 4.5') == 4.5
    assert clean_rating('4.2 Stars') == 4.2
    assert clean_rating('Invalid') is None

def test_transform_data():
    """Menguji transformasi keseluruhan data"""
    # Buat sample DataFrame
    sample_data = pd.DataFrame({
        'title': ['Shirt 1', 'Shirt 2', 'Shirt 1'],
        'price': ['Rp 100.000', '$50', 'Invalid'],
        'rating': ['Rating: 4.5', '4.2 Stars', 'Invalid'],
        'colors': ['Colors: 3', 'Colors: 2', 'Colors: 1'],
        'size': ['Size: M, L, XL', 'Size: S, M', 'Size: L'],
        'gender': ['Gender: Unisex', 'Gender: Male', 'Gender: Female']
    })
    
    # Transformasi
    transformed_df = transform_data(sample_data)
    
    # Validasi
    assert transformed_df['price'].iloc[0] == 1600000  # Konversi harga
    assert transformed_df['rating'].iloc[0] == 4.5  # Pembersihan rating
    assert transformed_df['colors'].iloc[0] == 3  # Ekstraksi jumlah warna
    assert transformed_df['size'].iloc[0] == 'M, L, XL'  # Pembersihan size
    assert transformed_df['gender'].iloc[0] == 'Unisex'  # Pembersihan gender

def test_transform_data_empty():
    """Menguji transformasi dengan DataFrame kosong"""
    empty_df = pd.DataFrame(columns=['title', 'price', 'rating', 'colors', 'size', 'gender'])
    
    transformed_df = transform_data(empty_df)
    
    assert len(transformed_df) == 0
    assert list(transformed_df.columns) == ['title', 'price', 'rating', 'colors', 'size', 'gender']