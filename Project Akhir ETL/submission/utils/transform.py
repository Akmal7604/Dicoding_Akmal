import pandas as pd
import re

def clean_price(price_str):
    """Bersihkan dan konversi harga ke Rupiah"""
    try:
        # Asumsi harga dalam USD, konversi dengan kurs Rp16.000
        price = float(re.sub(r'[^\d.]', '', price_str))
        return int(price * 16000)
    except (ValueError, TypeError):
        return None

def clean_rating(rating_str):
    """Bersihkan rating menjadi float"""
    try:
        return float(re.findall(r'\d+(?:\.\d+)?', rating_str)[0])
    except (IndexError, ValueError):
        return None

def transform_data(products_df):
    """
    Transformasi data produk
    
    Args:
        products_df (pd.DataFrame): DataFrame produk mentah
    
    Returns:
        pd.DataFrame: DataFrame produk yang telah dibersihkan
    """
    # Konversi kolom
    products_df['price'] = products_df['price'].apply(clean_price)
    products_df['rating'] = products_df['rating'].apply(clean_rating)
    
    # Bersihkan kolom lainnya
    products_df['colors'] = products_df['colors'].str.extract('(\d+)')[0]
    products_df['size'] = products_df['size'].str.replace('Size: ', '')
    products_df['gender'] = products_df['gender'].str.replace('Gender: ', '')
    
    # Hapus data duplikat dan null
    products_df = products_df.dropna()
    products_df = products_df.drop_duplicates()
    
    # Hapus produk yang tidak memiliki nama
    products_df = products_df[products_df['title'] != 'Unknown Product']
    
    return products_df