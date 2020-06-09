import numpy as np
import pandas as pd


## Merging two dataframes

filename1 = 'table1.csv'
filename2 = 'table2.csv'

try :
    
    df1 = pd.read_csv(filename1, engine='python')
    df2 = pd.read_csv(filename2, engine='python')
    
    print(df1.head(5))
    print(df2.head(5))
    
    print(df1.info())
    print(df2.info())
    
    print(df1.columns)
    print(df2.columns)
    
    
    # Merge the two tables into a big one.
    df_merged = pd.merge(df1, df2, on='user_id')  # on= tells on what column to merge the tables. if absent, it uses rwo id.
    
    print(df_merged)
    
    # alternative method
    df_merged2 = df1.merge(df2, on='user_id')
    
    
except FileNotFoundError :
    print('File not found.')
     
finally :
    pass
    