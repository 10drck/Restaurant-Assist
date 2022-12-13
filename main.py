import pandas as pd
import csv
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import json
import random 
import re
import sys

class RestaurantData():
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
                #print(order_ids, order_total)
                order_ids.append(order_id)
                order_total.append(total)
                order_id = self.df.loc[index, "Order Number"]
                quantity = self.df.loc[index, "Quantity"]
                product_price = self.df.loc[index, "Product Price"]
                total = 0
                total = total + (quantity * product_price)
    x = [order_ids, order_total]
    return x

    
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
        
    time_analysis(elements_count)
    
  def create_customer_bill(first_list, second_list):
      bill_list = [(first_list[i], second_list[i]) for i in range(0, len(first_list))]
      return bill_list
    
  def __str__ (bill_list):
      for bills in bill_list:
          for order_id in bills:
              return f"{order_id}"
            

def time_analysis(elements_count):
    """ take in elements_count dictionary run min() and max(); return as a variables max_hour and min_hour
    """
    #iterate through the dictionary; print the key with the highest value
    # iterate through the dictionary; print the key with the lowest value
    max_hour = [time for time, value in elements_count.items() if value == max(elements_count.values())]
    min_hour = [time for time, value in elements_count.items() if value == min(elements_count.values())]  

def write_file(x):
  """Using data from orders done in resturants, with the utilization of the pandas library
   be able to write to a csv to allow for spread sheet view.

  args:
    head_lst (lst): list containing the header names
    data_lst (lst): list containing the data
    can also be a dict
  """
  #replace with pandas code
  ids = x[0]
  totals = x[1]

  df = pd.DataFrame(
    {
      'ids': ids,
      'totals': totals
    }
  )
  df.to_csv('test.csv') #<- allocated file

def plot_data(data_csv):
  """Using the data that is passed through, plot a cohesive diagram for the owner to indicate trends in their resturant
  Args:
    data (list): list containing the data to plot
  """
  plt.figure(figsize =(10,10), dpi=100) # figure size for plotting 

  df = pd.read_csv(data_csv)
  df = df.drop(['Order Number', 'Order Date', 'Product Price', 'Total products'], axis=1) # drops columns for reading

  df = df.groupby(['Item Name'], as_index=False, sort=False).sum().sort_values(by=['Quantity'], ascending=False) # grouping to view quantities  
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
  #open the given file which is a csv
  with open(ordersFile, 'r' ) as file:
    df = pd.read_csv(file)
  
  #call Restaurant class to pass in the csv file
  restaurantdata = RestaurantData(df) 
  
  write_file(RestaurantData.order_total(restaurantdata))
  
  time_analysis(RestaurantData.peak_hours())
  
  print(RestaurantData.__str__())
  

  #time_analysis()
  customerinput = input(f"Would you like to see {args} as a plot? Yes or No")
  if customerinput.lower() == "yes":
    plot_data(ordersFile)
  elif customerinput.lower() == "no":
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
  parser.add_argument("file", help="file containing food items and stocks")
  
  return parser.parse_args(argslist)

if __name__ == '__main__':
  try:
    args = parse_args(sys.argv[1:])
  except ValueError as e:
    sys.exit(str(e))
  #print(args.file)
  main(args.file)

#any other functs youd like to run during the call.


  """
  Files being imported in:
    json file with the order, tip, person who ordered
    json file with staff members 
    
  Files being result/what's shown to operator:
    csv file will be written to about some of the data that is coming from the customers to view certain trends in different orders to help the resturant to bring in more reccuring customers and get more revenue.
    when presented the option, if the resturant owner would like to view  trends we will be able to present a plot containing some of that data trends found in the particular data through the utilization of the pandas library.
  """