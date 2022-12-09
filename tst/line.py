import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize =(10,10), dpi=100 )
def main():
  df = pd.read_csv('restaurant-1-orders.csv')
  df = df.drop(['Order Number', 'Product Price', 'Total products'], axis=1)
  df_without_date = df.drop(["Order Date"], axis=1)
  dfgroupedfood = df.groupby(['Item Name'], as_index=False, sort=False).sum().sort_values(by=['Quantity'], ascending=False)
  print(dfgroupedfood.head(1))


  df_without_name = df.drop(['Item Name'], axis=1)
  df["Order Date"] = pd.to_datetime(df["Order Date"])
  df3 = df_without_name.groupby(df['Order Date'].map(lambda x: x.year))
  print(df3.head(1))

  '''date = df['Order Date'].head(5)
  
  value = [10000,3,4,5,6]
  
  plt.plot(date, value)
  plt.xlabel('time')
  plt.ylabel('quantity')
  plt.savefig('data.png')'''


if __name__ == '__main__':
  main()