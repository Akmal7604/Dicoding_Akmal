import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def extract_product_data(product):
    """ Mengekstrak data produk dari satu elemen <div class='collection-card'> """
    try:
        title = product.find('h3', class_='product-title').text.strip()
        price = product.find('span', class_='price').text.strip()
        details = product.find('div', class_='product-details').find_all('p')
        rating = details[0].text.split(':')[-1].strip()
        colors = details[1].text.split(':')[-1].strip()
        size = details[2].text.split(':')[-1].strip()
        gender = details[3].text.split(':')[-1].strip()

        return {
            "timestamp": datetime.now().isoformat(),
            "title": title,
            "price": price,
            "rating": rating,
            "colors": colors,
            "size": size,
            "gender": gender
        }
    except AttributeError as e:
        logging.error(f"Gagal mengekstrak produk: {e}")
        return None

def fetch_page_content(url):
    """ Mengambil konten HTML dari URL dengan user-agent yang ditentukan """
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error saat mengambil {url}: {e}")
        return None

def scrape_fashion_studio():
    """ Melakukan scraping untuk data produk Fashion Studio dari halaman 1 hingga 50 dengan batas maksimal 1000 produk """
    base_url = "https://fashion-studio.dicoding.dev/page{}"
    all_products = []

    # Scrape halaman pertama
    first_page_url = "https://fashion-studio.dicoding.dev/"
    content = fetch_page_content(first_page_url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        products = soup.find_all('div', class_='collection-card')

        for product in products:
            if len(all_products) >= 1000:
                return all_products
            extracted_data = extract_product_data(product)
            if extracted_data:
                all_products.append(extracted_data)

    # Scrape halaman 2 hingga 50
    for page in range(2, 51):
        url = base_url.format(page)
        content = fetch_page_content(url)
        if not content:
            continue
        
        soup = BeautifulSoup(content, 'html.parser')
        products = soup.find_all('div', class_='collection-card')

        for product in products:
            if len(all_products) >= 1000:
                return all_products
            extracted_data = extract_product_data(product)
            if extracted_data:
                all_products.append(extracted_data)

    return all_products