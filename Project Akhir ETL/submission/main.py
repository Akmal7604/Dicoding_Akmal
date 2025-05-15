from utils.extract import scrape_fashion_studio
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets
import pandas as pd

def main():
    # Ekstrak
    raw_products = scrape_fashion_studio()
    
    # Transformasi
    products_df = pd.DataFrame(raw_products)
    cleaned_df = transform_data(products_df)
    
    # Load
    save_to_csv(cleaned_df)
    save_to_google_sheets(cleaned_df)

if __name__ == '__main__':
    main()