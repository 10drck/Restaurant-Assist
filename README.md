# Restaurant-Assist
## Table of Contents

+ [About](#about)
+ [Installing](#installing)
+ [Output](#output)
+ [Usage](#usage)
+ [Rubric](#rubric)

## About <a name = "about"></a>
Geared towards restaurants that wanted a program to showcase their selling points to current/potential stakeholders in their restaurant. Utilizing python makes this process seamless for restaurant owners to use and easily repersent varried statistics.




### Installing
--------------
### Prerequisites

1. [pandas](https://pandas.pydata.org/)
1. [matplotlib](https://matplotlib.org/)

Downlad libraries by typing in the following (or provided documentation from libraries):
``` python3
pip install pandas matplotlib
```

Clone the repository to your system:

``` python
$ git clone https://github.com/10drck/inst326_finalproj.git
```

To use the program, in the directory use the following command:

``` python
$ python3 restaurant_assist.py filename
```
On **Windows 8+**:
``` python
> python restaurant_assist.py filename
```

### Demostration
-----
For demonstration purposes, please subsitute filename with ` mock_resaurant_data.csv ` when running the program.

## Output

Files that may(or may not) be effected:
 - order_totals.csv
 - data.png
 <br>

If you would like to see the plot of your file. `data.png` will contain a bar plot of the top 7 dishes at your restaurant using the data provided by the .csv file. If you would like to see the totals of each order access ` order_totals.csv `.

 


## Usage <a name = "usage"></a>


For the temporary data we used [Kaggle](https://www.kaggle.com/datasets/henslersoftware/19560-indian-takeaway-orders) to imitate data from a restaurant.




### Rubric
----------------


| Name  | Methods/Functions  | Part D Reqs  | 
|---|---|---|
| Kendrick Montecino (10drck)  | - write_file() <br> - plot_data()  | - With statements <br> - Visualizing data (pyplot)   | 
| Sarah Peng (speng10) |- order_total() <br> - peak_hours()   | - RegEx <br> - Conditional statements  |
|Sophia Hrabinski  (sophrabin) |- time_analysis() <br> - \__str__()   | - Comprehension <br> - Magic method   |
|Lorenzo Regala (enzoregala)  |- main() <br> - parse_args()   | - Fstrings <br> - Parse args |  
### File Purposes
 1. __restaurant_assist.py__ - File where our main code is stored.
 2. __mock_restaurant_data.csv__ - CSV file that contains mock data that will be provided from a restaurant when using the program.
 3. __order_totals.csv__ - A CSV file that is being written to from the program. The written data will be the totals of different orders from the provided data.
 4. __data.png__(optional) - A PNG image that repersents a bar plot of the top 7 dishes pulled from the provided data (created from file).
 5. __README.md__ - Documentation on how to utilize the program.
 
