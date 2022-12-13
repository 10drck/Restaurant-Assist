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
    #print(self.df)
    
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
  df.to_csv('test.csv')
def main():
  df = pd.read_csv('restaurant-1-orders.csv')
  x = Customers(df)
  
  write_file(Customers.order_total(x))

main()