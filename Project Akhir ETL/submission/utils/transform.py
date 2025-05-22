import pandas as pd
import re

def clean_price(price_str):
    """Clean and convert price to float"""
    try:
        # Handle multiple price formats: Rp, $, etc.
        price_str = str(price_str)
        # Remove non-numeric characters except decimal point
        cleaned_price = re.sub(r'[^\d.]', '', price_str)
        
        # Check if the original string contains Rp or contains comma/dot
        if 'Rp' in price_str or '.' in price_str:
            # For Rupiah or dot-separated prices
            price = float(cleaned_price)
        else:
            # For dollar prices
            price = float(cleaned_price) * 16000
        
        return float(price * 16000)  # Always convert to Rupiah
    except (ValueError, TypeError):
        return None

def clean_rating(rating_str):
    """Clean rating to float"""
    try:
        # Ensure string conversion and extract first numeric value
        rating = re.findall(r'\d+(?:\.\d+)?', str(rating_str))
        return float(rating[0]) if rating else None
    except (IndexError, ValueError):
        return None

def clean_colors(colors_str):
    """Extract number of colors as integer"""
    try:
        # Extract numeric value
        colors = re.findall(r'\d+', str(colors_str))
        return int(colors[0]) if colors else None
    except (IndexError, ValueError):
        return None

def transform_data(products_df):
    """
    Transform product data
    
    Args:
        products_df (pd.DataFrame): Raw product DataFrame
    
    Returns:
        pd.DataFrame: Cleaned product DataFrame
    """
    # Create a copy to avoid SettingWithCopyWarning
    df = products_df.copy()
    
    # Convert columns with specific cleaning functions
    df['price'] = df['price'].apply(clean_price)
    df['rating'] = df['rating'].apply(clean_rating)
    df['colors'] = df['colors'].apply(clean_colors)
    
    # Clean size and gender columns
    df['size'] = df['size'].str.replace('Size: ', '', regex=False)
    df['gender'] = df['gender'].str.replace('Gender: ', '', regex=False)
    
    # Remove rows with any null values
    df = df.dropna(subset=['title', 'price', 'rating', 'colors'])
    
    # Remove duplicate rows based on specific columns
    df = df.drop_duplicates(subset=['title', 'price', 'rating'])
    
    # Remove products without a meaningful title
    df = df[df['title'] != 'Unknown Product']
    
    # Ensure correct data types
    df = df.astype({
        'title': 'object',
        'price': 'float64',
        'rating': 'float64',
        'colors': 'int64',
        'size': 'object',
        'gender': 'object'
    })
    
    return df