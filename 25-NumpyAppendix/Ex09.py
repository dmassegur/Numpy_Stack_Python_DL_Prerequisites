import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import *
from builtins import zip


## Ex9: Importing Ex6, Ex7 and Ex8 datasets into pandas and plotting them



def PlotDataframe(df, title):
    
    plt.scatter(df[:,0], df[:,1], c=df[:,2], s=40.0, alpha=0.3, label=title)
    plt.xlabel('feature x1')
    plt.ylabel('feature x2')
    plt.title(title+' dataset')
    plt.axis('equal') 
    plt.grid(True) 
    # plt.legend()
    plt.show()




t0 = datetime.now()


currDir = os.getcwd()
print(currDir)


filename = 'XOR'
extension = '.csv'

# Importing dataframe to pandas
df = pd.read_csv(currDir+'\\'+filename+extension).values
print(df.shape)
# plotting the dataframe
PlotDataframe(df, filename)


filename = 'Donuts'
extension = '.csv'

# Importing dataframe to pandas
df = pd.read_csv(currDir+'\\'+filename+extension).values
print(df.shape)
# plotting the dataframe
PlotDataframe(df, filename)


filename = 'Spiral'
extension = '.csv'

# Importing dataframe to pandas
df = pd.read_csv(currDir+'\\'+filename+extension).values
print(df.shape)
# plotting the dataframe
PlotDataframe(df, filename)



dt = datetime.now() - t0


print('')
print( 'Importing Ex6, Ex7 and Ex8 datasets to Pandas and plotting, elapsed time: %0.4f seconds.' %(dt.total_seconds()) )
