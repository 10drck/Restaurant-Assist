import pandas as pd
import csv
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import json
import random 
import re

class Restaurant():
  """Creates a customer  object that can order food. Takes information of customer, what the order is, and time the order is made.
  
  Attributes: 
    name(str): name of the customer
    phone(str): customers phone number
    payment_type(str): customers payment type
    order(list): what the customer orders
    time(int): the time that the customer ordered

  """
  def __init__(self, data_frame):
    """Create and populate the object of customers using name, phone, payment_type,
    order, order_num, and time that will be passed through when intialized
    
    Args:
        name (str): name of the customer
        phone (str): phone number of the customer
        payment (str): how they will pay
        order (list): the customers order default to an empty list []
        order_num (int): the order number 
        time (int): the hour they ordered in
    
    Side effects: 
        Creates Restaurant attribute
    """
    
    self.df = data_frame
    
  def order_total(self):
    """Takes in the customers order and checks if it is available 
    and calculates the total cost of their bill
        
    Args:
        order(lst): the order of the customer
        
    Returns: the total cost of their bill
    """
    order_id = self.df.loc[0, "Order Number"]
    #print("orderid", order_id)
    order_ids = []
    order_total = []
    for index in range(len(self.df)):
        if index == 0:
            order_id = self.df.loc[index, "Order Number"]
            quantity = self.df.loc[index, "Quantity"]
            product_price = self.df.loc[index, "Product Price"]
            total = quantity * product_price
        else:
            if order_id == self.df.loc[index, "Order Number"]:
                quantity = self.df.loc[index, "Quantity"]
                product_price = self.df.loc[index, "Product Price"]
                total = total + (quantity * product_price)
            else:
              #how to write to csv file?
                print(order_id, total)
                order_ids.append(order_id)
                order_total.append(total)
                write_file(order_ids, order_total)
                order_id = self.df.loc[index, "Order Number"]
                quantity = self.df.loc[index, "Quantity"]
                product_price = self.df.loc[index, "Product Price"]
                total = 0
                total = total + (quantity * product_price)

    
  def peak_hours(self):
    """Summary: calcuates the time of day that orders are most commonly made
    
    Args: 
        time(int): the hour that the order is made in 
        
    Returns:
      the most orders in the hour
    """
    
    times_list = []

    for index in range(len(self.df)):
        if index == 0:
            order_id = self.df.loc[index, "Order Number"]
            date = self.df.loc[index, "Order Date"]
            match = re.search(r"(\d{1,2}\/)(\d{1,2}\/\d{2,4} )(\d{1,2})(:\d{1,2})", date)
            hour = match.group(3)
            times_list.append(hour)
        else:
            if order_id != self.df.loc[index, "Order Number"]:
                date = self.df.loc[index, "Order Date"]
                match = re.search(r"(\d{1,2}\/)(\d{1,2}\/\d{2,4} )(\d{1,2})(:\d{1,2})", date)
                hour = match.group(3)
                times_list.append(hour)
                order_id = self.df.loc[index, "Order Number"]
        
    elements_count = {}

    for element in times_list:
        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1
    for key, value in elements_count.items():
        print(f"{key}:{value}")
        
    max_value = max(elements_count.values())
    # print(max_value)
    # print(elements_count.items(max_value))

    #print(len(times_list))
    
  
class Restaurant():
  """This creates the restaurant class that is the basics of the restaurant
            
  Attributes:
      menu_items (dict): the items on the menu 
      inventory (dict): the menu items and the amount left that they have 
  """
  def __init__(self,inventory):
    """Create and populates the object for resurants using the location, name, and inventory of said insitution
    Args:
        inventory (dict): this is an inventory of all of the food items that the 
        restaurant has in stock
        
    """ 
    self.inventory = inventory 
    #create the inventory     
    inventory = {(self.menu_item, random.randint(0,50))}
    
    #create the list of menu items as an attribute 
    self.menu_items = pd.read_json("menu.json")
    self.menu_items = list(self.menu_items.keys())
  
  def check_availability(self, inventory):
    """ uses list comprehension to add dictionary keys to a list in order to determine if an item is out of stock 
       Args: 
          inventory (dict):value: the remaining food in the restaurant keys: amount of the item (int)
          order_list (lst): list of input orders 
       Returns: 
          updates the inventory dictionary 
          prints out out of stock items 
     """
    
    #create a list of the ordered items 
    order_list = list(pd.read_csv('resturant-1-orders.csv', usecols = ["Item Name"]))
    
    #update the inventory for each order 
    [inventory.values()-=1 for orders in order_list if inventory.values() >= 1] 
    
    #print out if an order is out of stock
    for orders in order_list:
      if inventory.values() == 0:
        print(f"{inventory.keys()} is out of stock")

  
  def profit(self):
    """Calculates the profit at the end of the month, creates a csv file with relevant information 
    expenses - revenu (printed by the orders_total) 

       Args: 
            Orders_total (int): the combined total money from the orders 
      Returns: 
        profit as plain text 
        monthly_profit(csv df): total profits for the day
    """
    #create the two dataframes out of the csv files
    revenue_df = pd.read_csv('resturant-1-orders.csv', usecols = ["orders_total"])
    cost_df = pd.read_csv("resturant_costs.csv")
    
    #calculate the profit 
    profit = list(revenue_df.sum() - cost_df.sum())
    
    # return profit 
    return profit 
    #write to a new file (can't write to the main file, it isn't sorted by the order number)
    write_file()
    
  
  

def write_file(head_lst, data_lst):
  """Using data from orders done in resturants, with the utilization of the pandas library
   be able to write to a csv to allow for spread sheet view.

  args:
    head_lst (lst): list containing the header names
    data_lst (lst): list containing the data
    can also be a dict
  """
  #replace with pandas code

  with open('.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(head_lst) # write the header
    writer.writerows(data_lst) # write mutiple rows.
    #can also use dicts 

def plot_data(data_csv):
  """Using the data that is passed through, plot a cohesive diagram for the owner to indicate trends in their resturant

  Args:
    data (list): list containing the data to plot
  """
  plt.figure(figsize =(10,10), dpi=100) # figure size for plotting 

  df = pd.read_csv(data_csv)
  df = df.drop(['Order Number', 'Order Date', 'Product Price', 'Total products'], axis=1) # drops columns for reading

  df = df.groupby(['Item Name'], as_index=False, sort=False).sum().sort_values(by=['Quantity'], ascending=False) # grouping to view quantities
  #print(df.head(3))
  
  plt.bar(x=df['Item Name'].head(7), height=df['Quantity'].head(7))
  plt.savefig('data.png') # saves to directory as 'data.png'
  print('Done with the graph!')
    


def main(ordersFile):
  """intialize objects in this code, call for pandas implimentation for data after the day.

  args:
    name(str): the name of either the customer or the employee operating
    access_code(int): the access code of the employee
  """
  #funct will call for functs and classes
  
  #time_analysis()
  
  #open the given file which is a csv
  with open(ordersFile, 'r' ) as file:
    df = pd.read_csv(file)
  
  #call Restaurant class to pass in the csv file
  Restaurant(df)

  #time_analysis()
  customerinput = input(f"Would you like to see {filename} as a plot? Yes or No")
  if customerinput.lower() == "yes" or "y":
    plot_data()
  elif customerinput.lower() == "no" or "n":
    pass
  else:
    print("That was an invalid input")
  
def parse_args(argslist):
  """Parse command line arguments

  Args:
      args (string): command line arguments
      
  Returns: 
      args: parsed arguments
  """
  parser = ArgumentParser()
  parser.add_argument("filepath", help="file containing food items and stocks")
  parser.add_argument("column", help="column from the file")

  args = parser.parse_args(argslist)
  if args.filepath is None:
    raise ValueError("Missing filepath")
  if args.column is None:
    raise ValueError("Name of Column?")
  return args

if __name__ == '__main__':
  filename = parse_args()
  main(filename)
  

#any other functs youd like to run during the call.


  """
  Files being imported in:
    json file with the order, tip, person who ordered
    json file with staff members 
    
  Files being result/what's shown to operator:
    csv file will be written to about some of the data that is coming from the customers to view certain trends in different orders to help the resturant to bring in more reccuring customers and get more revenue.

    when presented the option, if the resturant owner would like to view  trends we will be able to present a plot containing some of that data trends found in the particular data through the utilization of the pandas library.
  """
