import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import logging
import sys
from pathlib import Path

# Tambahkan root project ke path
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

from utils.extract import (
    extract_product_data, 
    fetch_page_content, 
    scrape_fashion_studio,
    HEADERS
)


def create_mock_product_html():
    """Membuat HTML produk palsu untuk testing"""
    return """
    <div class='collection-card'>
        <h3 class='product-title'>Test Shirt</h3>
        <span class='price'>$100.00</span>
        <div class='product-details'>
            <p>Rating: ⭐ 5 / 5</p>
            <p>Colors: 5 Colors</p>
            <p>Size: M</p>
            <p>Gender: Unisex</p>
        </div>
    </div>
    """

def test_extract_product_data():
    """Menguji ekstraksi data produk"""
    # Buat BeautifulSoup object dari HTML palsu
    soup = BeautifulSoup(create_mock_product_html(), 'html.parser')
    product = soup.find('div', class_='collection-card')
    
    # Ekstrak data
    result = extract_product_data(product)
    
    # Validasi struktur data
    assert result is not None
    assert 'timestamp' in result
    assert result['title'] == 'Test Shirt'
    assert result['price'] == '$100.00'
    assert result['rating'] == '⭐ 5 / 5'
    assert result['colors'] == '5 Colors'
    assert result['size'] == 'M'
    assert result['gender'] == 'Unisex'

def test_extract_product_data_incomplete():
    """Menguji ekstraksi produk dengan data tidak lengkap"""
    # HTML tidak lengkap
    incomplete_html = """
    <div class='collection-card'>
        <h3 class='product-title'>Incomplete Shirt</h3>
    </div>
    """
    soup = BeautifulSoup(incomplete_html, 'html.parser')
    product = soup.find('div', class_='collection-card')
    
    # Ekstrak data
    with patch('logging.error') as mock_log:
        result = extract_product_data(product)
        
        # Seharusnya mengembalikan None dan mencatat error
        assert result is None
        mock_log.assert_called_once()

def test_fetch_page_content():
    """Menguji fungsi fetch_page_content"""
    # Mock requests.get
    with patch('requests.get') as mock_get:
        # Buat mock response
        mock_response = MagicMock()
        mock_response.content = b"<html>Test Content</html>"
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response
        
        # Panggil fungsi
        result = fetch_page_content("https://test-url.com")
        
        # Validasi
        assert result == b"<html>Test Content</html>"
        mock_get.assert_called_once_with("https://test-url.com", headers=HEADERS)

def test_fetch_page_content_error():
    """Menguji error handling pada fetch_page_content"""
    # Mock requests.get untuk melempar exception
    with patch('requests.get') as mock_get:
        # Simulasi RequestException
        mock_get.side_effect = requests.exceptions.RequestException("Test Error")
        
        # Panggil fungsi
        with patch('logging.error') as mock_log:
            result = fetch_page_content("https://test-url.com")
            
            # Validasi
            assert result is None
            mock_log.assert_called_once()

@patch('utils.extract.fetch_page_content')
@patch('utils.extract.BeautifulSoup')
def test_scrape_fashion_studio_basic(mock_beautifulsoup, mock_fetch):
    """Menguji proses scraping dasar"""
    # Persiapan mock
    mock_content = b"<html>Mock Content</html>"
    mock_fetch.return_value = mock_content
    
    # Buat mock soup dengan produk palsu
    mock_soup = MagicMock()
    mock_product = BeautifulSoup(create_mock_product_html(), 'html.parser').find('div', class_='collection-card')
    mock_soup.find_all.return_value = [mock_product] * 10  # 10 produk palsu
    mock_beautifulsoup.return_value = mock_soup
    
    # Panggil fungsi scraping
    results = scrape_fashion_studio()
    
    # Validasi
    assert len(results) == 10  # Sesuai jumlah produk palsu
    
    # Pastikan setiap produk memiliki struktur yang benar
    for result in results:
        assert 'timestamp' in result
        assert 'title' in result
        assert 'price' in result
        assert 'rating' in result
        assert 'colors' in result
        assert 'size' in result
        assert 'gender' in result