import matplotlib.pyplot as plt
import pandas as pd
 
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)

# Membuat DataFrame dan mengurutkan data


def bar_vertikal():
  plt.bar(x=cities, height=populations) #bar chart vertikal
  plt.xticks(rotation=45) #rotasi label
  plt.show()

def bar_horizontal():
  plt.barh(y=cities, width=populations) #bar chart horizontal
  plt.show()
  
def bar_sort_population():
  df = pd.DataFrame({
    'Cities': cities,
    'Population': populations,
  })
  df.sort_values(by='Population', inplace=True)
  plt.barh(y=df["Cities"], width=df["Population"])
  plt.xlabel("Population (Millions)")
  plt.title("Population of Cities in Indonesia")
  plt.show()

bar_sort_population()  