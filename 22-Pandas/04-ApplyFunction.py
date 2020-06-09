import numpy as np
import pandas as pd
from datetime import time, datetime


# datetime.strptime converts a string into a date format
print(datetime.strptime('1949-05','%Y-%m')) 


## Assigning new columns with different values --> apply() function

filename = 'international-airline-passengers.csv'
try : 
    print('Attempting to open file: %s.' %filename)
    df = pd.read_csv(filename, engine='python', skipfooter=3)  # by default pandas assigns the first row of the file as a header, if no header argument is added. We also want to skip the last 3 rows but this only works with engine python.
    print('Reading data from file...')
    
    # Print the headers:
    print(df.columns) 
    
    # Rename columns:
    df.columns = ['Month', 'Passengers']
    print(df.columns)
    
    # Print the values of a named column:
    print(df['Passengers'])
    print(df.Passengers)  # does the same  but this only works if the column header does not have spaces!
    
    
    # Adding a bias column:
    df['ones'] = 1
    
    print(df.head())
    
    
    # Apply a function to a new column:
    # in this case we convert the first column (month) into a date format in a new column called dt
    df['dt'] = df.apply(lambda row : datetime.strptime(row['Month'], '%Y-%m'), axis=1)  # axis=1 is column
    
    print(df.head())
    print(df.info())
    
         
    
except FileNotFoundError :
    print('File %s not found.' %filename)

finally :
    pass