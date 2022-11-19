import pandas as pd
import csv
import matplotlib.pyplot as plt

class Customers():
  """Creates a customer object that can order food
  
  Attributes: 
    name(str): name of the customer
    phone(str): customers phone number
    payment_type(str): customers payment type
    order(list): what the customer orders
    order_num(int): order number for the customer
    time(int): the time that the customer ordered

  """
  def __init__(self, name, phone, payment_type, order, order_num, time):
    """Create and populate the object of customers using name, phone, payment_type,
    order, order_num, and time that will be passed through when intialized
    
    Args:
        name (str): name of the customer
        phone (str): _description_
        payment (str): how they will pay
        order (list): the customers order default to an empty list []
        order_num (int): the order number 
        time (int): the hour they ordered in
    
    Side effects: 
        Creates Customers attribute
    """
    pass
  
  def orders(order):
    """Takes in the customers order and checks if it is available 
    and calculates the total cost of their bill
        
    Args:
        order(lst): the order of the customer
        
    Returns: the cost of their bill and if there are any items not available
    """
  
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
    pass
  
  def check_availability():
    """Filters the inventory csv against the order list 
       Args: 
          inventory (dict): the remaining food in the restaurant 
          order(dict): the order that was input 
       Returns: 
          in_stock (boolean): inside an f-string, returns if the item is out of stock 
     """
    pass
  
  def profit():
    """Calculates the profit at the end of an ordering day 
       Args: 
            Orders_total (int): the combined total money from the orders 
            Staff_wages (int): the combined total wages of the staff for the day 
            Passive_costs (int): set cost of the restaurant bills (rent, electric, etc) set arbitrability by us 
      Returns: 
        Daily_profit(int): total profits for the day
    """
    pass
  
  def peak_hours(time):
    """Summary: calcuates the time of day that orders are most commonly made
    
    Args: 
        time(int): the hour that the order is made in 
        
    Returns:
      the most orders in the hour
    """
    pass
  
class Staff(Restaurant):
  """Summary: This creates a staff object that is the subclass of the restaurant

  Args:
      Restaurant (class): the restaurant class, to inherit all of attributes of
                        restaurant
  """
  def __init__(name, hours):
    """this takes in the name and hours of the staff member

    Args:
        name (str): name of the staffers
        hours (int): hours worked
    """
  pass
  
  def __add__(staff, tip):
    """Summary: this adds tips to the given staff waiter
    
    Args: 
      staff(string): name of the staff 
      tip(int): the tip they received from an order
      
    return: staff member with increase tip amount 
    """
    pass
  
  def tips(orders):
    """summary: takes in the tips from the order
    
    args: 
        orders(string): the order with the total and tip
        
    return:
        the tip for the staff member
    """
    pass


def write_file(head_lst, data_lst):
  """Using data from orders done in resturants, with the utilization of the pandas library
   be able to write to a csv to allow for spread sheet view.

  args:
    head_lst (lst): list containing the header names
    data_lst (lst): list containing the data
    can also be a dict
  """
  pass

def plot_data(data):
  """Using the data that is passed through, plot a cohesive diagram for the owner to indicate trends in their resturant

  Args:
    data (list): list containing the data to plot
  """
  pass


def main(name, access_code = None):
  """intialize objects in this code, call for pandas implimentation for data after the day.

  args:
    name(str): the name of either the customer or the employee operating
    access_code(int): the access code of the employee
  """
  #funct will call for functs and classes
  pass #<-temp
  
def parse_args(args):
  """Parse command line arguments

  Args:
      args (string): command line arguments
      
  Returns: 
      args: parsed arguments
  """

  if __name__ == '__main__':
    main()
  #any other functs youd like to run during the call.


  """
  Files being imported in:
    json file with the order, tip, person who ordered
    json file with staff members 
    
  Files being result/what's shown to operator:
    csv file will be written to about some of the data that is coming from the customers to view certain trends in different orders to help the resturant to bring in more reccuring customers and get more revenue.

    when presented the option, if the resturant owner would like to view such trends we will be able to present a plot containing some of that data trends found in the csv file parsed using the pandas library.
  """