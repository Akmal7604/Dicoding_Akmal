import pandas as pd
import matplotlib.pyplot as plt
import requests
 
url = 'https://query1.finance.yahoo.com/v8/finance/chart/BBCA.JK?events=capitalGain%7Cdiv%7Csplit&formatted=true&includeAdjustedClose=true&interval=1d&period1=1704165596&period2=1735689600&symbol=BBCA&userYfid=true&lang=en-US&region=US'
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
 
# Ambil data dari URL
response = requests.get(url, headers=headers)
 
# Konversi data JSON menjadi DataFrame
data = response.json()
 
# Ekstraksi data dari JSON
timestamps = data['chart']['result'][0]['timestamp']
indicators = data['chart']['result'][0]['indicators']['quote'][0]
 
# Membuat DataFrame
df = pd.DataFrame({
    'timestamp': pd.to_datetime(timestamps, unit='s'),
    'open': indicators['open'],
    'high': indicators['high'],
    'low': indicators['low'],
    'close': indicators['close'],
    'volume': indicators['volume'],
})
 
plt.figure(figsize=(12, 5))
plt.plot(df['timestamp'], df['close'], color='red')
plt.xlabel('Date',size=15)
plt.ylabel('Price',size=15)
plt.show()