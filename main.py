import pandas as pd
import csv
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import json
import random 
import re

class Customers():
  """Creates a customer object that can order food. Takes information of customer, what the order is, and time the order is made.
  
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
        Creates Customers attribute
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
    for index in range(len(df)):
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
      location(str): the location of the restaurant
      name(str): the name of the restaurant
      inventory(dict): nested dictionaries
  """
  def __init__(self, location, name, inventory):
    """Create and populates the object for resurants using the location, name, and inventory of said insitution

    Args:
        location (str): the location of the restaurant, address
        name (str): the name of the restaurant
        inventory (dict): this is an inventory of all of the food items that the 
        restaurant has in stock
    """
    self.location = location
    self.name = name
    self.inventory = inventory
  
  def check_availability():
    """Filters the inventory csv against the order list 
       Args: 
          inventory (dict): the remaining food in the restaurant 
          order(dict): the order that was input 
       Returns: 
          in_stock (boolean): inside an f-string, returns if the item is out of stock 
     """
    inventory = {(self.menu_item, random.randint(0,50))}
    order_list = list(orders.keys())
    final_list = [print(f"{inventory.keys()} is out of stock") 
    for orders in order_list if inventory.values() == 0]
    inventory[:][1] = inventory[:][1] - 1; 
  
  def profit():
    """Calculates the profit at the end of an ordering day 
       Args: 
            Orders_total (int): the combined total money from the orders 
            Staff_wages (int): the combined total wages of the staff for the day 
            Passive_costs (int): set cost of the restaurant bills (rent, electric, etc) set arbitrability by us 
      Returns: 
        Daily_profit(int): total profits for the day
    """
    revenue_df = pd.read_csv('orders_total.csv')
    cost_df = pd.read_csv("resturant_costs.csv")
    revenue_df.sum() - cost_df.sum()

    with open('file_I_havent_made_yet', 'w') as profit_csv:
      writer = csv.writer(profit_csv)
      writer.writerow("")
  
  

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

def plot_data(data):
  """Using the data that is passed through, plot a cohesive diagram for the owner to indicate trends in their resturant

  Args:
    data (list): list containing the data to plot
  """
  #plt.bar(left, values, tick_label = tick_label, width = .9, color = x) <- bar
  #could use pie (show margins) or line for other data
    


def main(ordersFile, ):
  """intialize objects in this code, call for pandas implimentation for data after the day.

  args:
    name(str): the name of either the customer or the employee operating
    access_code(int): the access code of the employee
  """
  #funct will call for functs and classes
  #open the given file which is a csv
  with open(ordersFile, 'r' ) as file:
    df = pd.read_csv(file)
    
  with open(menu, 'r', encoding = 'utf-8') as f:
        menu = json.load(f)
  #call customers class to pass in the csv file
  Customers(df)
  
def parse_args(argslist):
  """Parse command line arguments

  Args:
      args (string): command line arguments
      
  Returns: 
      args: parsed arguments
  """
  parser = ArgumentParser()
  parser.add_argument("filepath")
  parser.add_argument("column")

  args = parser.parse_args(argslist)
  if args.filepath is None:
    raise ValueError("Missing filepath")
  if args.column is None:
    raise ValueError("Name of Column?")
  return args

if __name__ == '__main__':
  main()
  parse_args()
#any other functs youd like to run during the call.


  """
  Files being imported in:
    json file with the order, tip, person who ordered
    json file with staff members 
    
  Files being result/what's shown to operator:
    csv file will be written to about some of the data that is coming from the customers to view certain trends in different orders to help the resturant to bring in more reccuring customers and get more revenue.

    when presented the option, if the resturant owner would like to view  trends we will be able to present a plot containing some of that data trends found in the particular data through the utilization of the pandas library.
  """
