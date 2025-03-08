import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
customers_df.head()
# print(customers_df.head())

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
orders_df.head()
# print(orders_df.head())

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
product_df.head()
# print(product_df.head())

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
sales_df.head()
# print(sales_df.head())

def infoCustomers():
  customers_df.info() # menampilkan informasi data
  print(customers_df.isna().sum()) # menampilkan jumlah data NaN
  print("Jumlah duplikasi: ", customers_df.duplicated().sum()) # menampilkan jumlah data duplikat
  print(customers_df.describe()) # menampilkan statistik deskriptif

def infoOrders():
  orders_df.info() # menampilkan informasi data
  print("Jumlah duplikasi: ",orders_df.duplicated().sum()) # menampilkan jumlah data duplikat
  print(orders_df.describe()) # menampilkan statistik deskriptif

def infoProduct():
  product_df.info() # menampilkan informasi data
  print("Jumlah duplikasi: ", product_df.duplicated().sum()) # menampilkan jumlah data duplikat
  print(product_df.describe()) # menampilkan statistik deskriptif

def infoSales():
  sales_df.info() # menampilkan informasi data
  print(sales_df.isna().sum()) # menampilkan jumlah data NaN
  print("Jumlah duplikasi: ", sales_df.duplicated().sum()) # menampilkan jumlah data duplikat
  print(sales_df.describe()) # menampilkan statistik deskriptif
  print(sales_df[sales_df.total_price.isna()]) # menampilkan data yang memiliki nilai NaN

# infoCustomers()
# infoOrders()
# infoProduct()
# infoSales()

# Membersihkan data pada customers_df
customers_df.drop_duplicates(inplace=True) # menghapus data duplikat
customers_df[customers_df.gender.isna()], # menampilkan data yang memiliki nilai NaN
customers_df.gender.value_counts() # menampilkan jumlah data yang unik
customers_df.fillna(value="Prefer not to say", inplace=True) # mengisi data NaN dengan nilai "Prefer not to say"
customers_df.age.replace(customers_df.age.max(), 70, inplace=True) # mengganti nilai tertinggi dengan nilai 70
customers_df.age.replace(customers_df.age.max(), 50, inplace=True) # mengganti nilai tertinggi dengan nilai 50

# Membersihkan data pada orders_df
datetime_columns = ["order_date", "delivery_date"] # kolom yang bertipe datetime
for column in datetime_columns:
  orders_df[column] = pd.to_datetime(orders_df[column]) # mengubah tipe data menjadi datetime

# Membersihkan data pada product_df
product_df.drop_duplicates(inplace=True) # menghapus data duplikat

# Membersihkan data pada sales_df
sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"] # menambahkan kolom total_price




######################################### Explanatory Data Analysis #########################################

print(customers_df.describe(include="all")) # menampilkan statistik deskriptif

customers_df.groupby(by="gender").agg({
    "customer_id": "nunique",
    "age": ["max", "min", "mean", "std"]
}) # menampilkan statistik deskriptif berdasarkan gender

customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False)
customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=False)

print (customers_df.all)






