import pandas as pd
import csv
import matplotlib.pyplot as plt

class Customers():
  """Creates a customer object that can order food
  
  Attributes: 
    Name(str): name of the customer
    phone number (string): customers phone number
    payment method (str): how they will pay
  """
  def __init__(self, name, phone, payment, order, order_num, time):
    """Summary: takes in the name, phone number, payment method, order
    
    Args:
        name (str): name of the customer
        phone (str): _description_
        payment (str): how they will pay
        order (list): the customers order default to an empty list []
        order_num (_type_): the order number 
        time (_type_): the hour they ordered in 
    
    Side effects: 
        assigns the name, phone number, payment method and order
    """
    pass
  
  def orders(order):
    """Takes in the customers order and checks if it is available and
        total cost of their bill
        
    Args:
        order(lst): the order of the customer
        
    Returns: the cost of their bill and if there are any items not available
    """
  
def main():
  #funct will call for functs and class
  pass #<-temp


def write_file(head_lst, data_lst):
  """
  using data found inside program writes to a csv file

  args:
    head_lst (lst): list containing the header names
    data_lst (lst): list containing the data
    can also be a dict
  """
  with open('.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)

    writer.writerow(head_lst) # write the header

    writer.writerows(data_lst) # write mutiple rows.
#can also use dicts 

if __name__ == '__main__':
  main()
  #any other functs youd like to run during the call.
  
def parse_args(args):
  """take in command line arguments

  Args:
      args (string): command line arguments
  """