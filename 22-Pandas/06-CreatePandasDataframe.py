import pandas as pd
import numpy as np


## How to create a dataframe:

df = pd.DataFrame([ [1,'david',500] , [2,'marija',250] ])  ## without headers added
print(df[0:2])  # prints columns 1 to 3
print(df[0])  # prints first column

    
data = [ [1,'david',500] , [2,'marija',250] ]
df = pd.DataFrame(data, columns=['id','name','savings'])  ## headers added

## Add a row to the df:
#### df = pd.append(df, [[3,'maksim',150],[4,'damia',100]])  #wrong!!!!
# using column names:
# df = pd.append( df, {'id': 3, 'name': 'maksim', 'savings': 150} )
df = df.append( {'id': 3, 'name': 'maksim', 'savings': 150}, ignore_index = True )  # it will append it at the bottom
df = df.append( pd.Series( [4,'damia',100], index = df.columns ), ignore_index = True )
df.loc[50] = [6,'jon',125]  # it will store index 50 but it will still be in row 4

print('')
print(df)
print('')
print(df.info())
print('')
print(df[0:1])  ## column indexing doesn't work now because this df has headers!!!!
print('')
print(df.columns[0:2])  ## prints headers 1 to 3
print('')
print(df.columns)  # to print the headers
print('')
print(df.iloc[4])  # iloc prints row id!!!!
# print('')
# print(df.ix[50])  # ix print index id!!!!  OBSOLETE!!
print('')
print(df.loc[50])  # ix print index id!!!!


# dataframe with index different than row id:
data = [[1,'david',500],[2,'marija',250]]
df = pd.DataFrame(data, columns=['id','name','savings'], index=['a','b'])  ## column headers and row indices added
print('')
print(df)
print('')
print(df.iloc[1])  # prints by row id
print('')
print(df.loc['a'])  # prints by index id

