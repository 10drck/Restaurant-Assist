import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize =(10,10), dpi=100 )
def main():
  df = pd.read_csv('restaurant-1-orders.csv')
  df = df.drop(['Order Number', 'Order Date', 'Product Price', 'Total products'], axis=1)
  df = df.groupby(['Item Name'], as_index=False, sort=False).sum().sort_values(by=['Quantity'], ascending=False)
  #print(df.head(3))
  
  plt.bar(x=df['Item Name'].head(7), height=df['Quantity'].head(7))
  plt.savefig('data.png')
  print('Done with the graph!')


if __name__ == '__main__':
  main()