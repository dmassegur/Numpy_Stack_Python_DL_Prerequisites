import numpy as np


## Attempting to read data from a file:

filename = 'data_2d.csv'
try : 
    print('Attempting to open file: %s.' %filename)
    file = open(filename,'r')
    print('Reading data from file...')
    
#     l = file.readline()
#     count = 1
#     while len(l)>0 :
#         # print(l)
#          
#         print('Number of read rows in the file: ', count)
#         a = np.array(l.split(','))
#         print('A:\n',a)
# 
#         l = file.readline()
#         count += 1

#     A = np.array([])
#     count = 0
#     for l in file :
# #         print(l)
#         count += 1 
# #         print('Number of read rows in the file: ', count)
#         # l.replace('\n','')  #useless
#         a = np.array(l.split(','))   # converting read line to array of strings
# #         print(type(a))
#         a = np.char.replace(a,'\n','')
#         
#         a = a.astype(np.float)   # converting array to float terms
# #         print(type(a))
# 
#         A = np.append(A,a,0)   # appending array into the matrix
# #         print(type(A))


    A = []
    count = 0
    for l in file :
#         print(l)
        count += 1 
#         print('Number of read rows in the file: ', count)
        row = l.split(',')   # converting read line to list of strings
#         print(type(row))
        # row = [r.replace('\n','') for r in row]  # not needed
#         print(row)
#         print(type(row))
        sample = list(map(float, row))  # converting the list of strings to list of floats  
        sample = [float(i) for i in row]  # alternative!!!
#         print(sample)
        A.append(sample)   # appending listo into the vector of lists
#         print(type(A))
    
#     print(A)
    A = np.array(A)  # converting vector of lists into matrix
#     print(type(A))
    print( 'Number of read rows in the file:', count )
    print( 'Read data from file stored into this matrix:\n',A )    
    print( 'Dimensions of the dataset: %d rows (samples) and %d columns (features).' %(A.shape[0], A.shape[1]) )    
        
    
except FileNotFoundError :
    print('File %s not found.' %filename)

finally :
    file.close()
