import numpy as np
import pandas as pd


## Attempting to read headed csv file in pandas:

filename = 'international-airline-passengers.csv'
try : 
    print('Attempting to open file: %s.' %filename)
    df = pd.read_csv(filename, engine='python', skipfooter=3)  # by default pandas reads the header if no header argument is added, we also want to skip the last 3 rows but this only works with engine python.
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
    

             
    
except FileNotFoundError :
    print('File %s not found.' %filename)

finally :
    pass
