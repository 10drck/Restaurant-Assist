import pandas as pd
import csv

#class Order():
  
#class Receipt():
  
#class Inventory():
  
#class Staff():

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