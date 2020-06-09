import numpy as np
import pandas as pd


## Attempting to read dataframe from a file in pandas:

filename = 'data_2d.csv'
try : 
    print('Attempting to open file: %s.' %filename)
    A = pd.read_csv(filename, header=None)  # header=None treats the first row of the file as data and not as headers
    print('Reading data from file...')
    
    print(type(A))
    print(A.info())
    print(A.head())  # read the first few roads
    print(A.head(10))  # read the first 10 rows
    print(A.shape[0])  # number of rows


    ## convert dataframe into matrix array
    # M = A.as_matrix()  # convert dataframe into array  # obsolete!!
    M = A.values  # convert dataframe into array  # replaces as_matrix()!!
    print(type(M))
    
    
    # print index 0 is different in pandas vs numpy
    print( A[0] )  # pandas dataframe prints the column!
    print( type(A[0]) )  # each column is a series

    print( M[0] )  # numpy prints row!
    
    
    # print row in pandas
    print( A.iloc[0] )  # prints pandas row id!! this is a series too
    print( A.ix[0] )  # prints pandas index id (row header), not the row!!  obsolete
    print( type(A.ix[0]) )  # each column is a series
    print( A.loc[0] )  # prints pandas index id (row header), not the row!!  same as ix
    
    # print various columns
    print( A[[0,2]] )  # prints column 0 and 2
    
    # select specific rows
    print( A[ A[0] < 5 ] )  # prints all rows with values in column 0 lower than 5
    
    print( A[0] < 5 )  # prints what rows satisfy values in column 0 lower than 5
    
    
    # how to select a single element with index i,j
#     b = A.iloc[0]
#     print(b)
#     print(b.iloc[0])
    print(A.iloc[0].iloc[0])  # column then row
    
    print(A.head(3))
    
    

#     print( 'Number of read rows in the file:', A.shape[0] )
#     print( 'Read data from file stored into this matrix:\n',A )    
#     print( 'Dimensions of the dataset: %d rows (samples) and %d columns (features).' %(A.shape[0], A.shape[1]) )    
         
    
except FileNotFoundError :
    print('File %s not found.' %filename)

finally :
    pass
