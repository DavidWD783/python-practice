# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:$PATH"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import url for table
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tb.csv'
urlretrieve(url, 'tb.csv')

df = pd.read_csv(url, sep=',')
# print(df.head())

# Melt age and sex columns into new table
melted = pd.melt(df, id_vars = ['country', 'year'], value_vars = ['m014', 'm1524'], value_name = 'value')
print(melted.head())

# Create new column for sex using string value from variable
melted['sex'] = melted.variable[0][0]

# Pivot table on m014 and m1524
pivoted = melted.pivot_table(values = 'value', index = ['country', 'year', 'sex'], columns = 'variable', aggfunc = np.mean)
pivoted = pivoted.reset_index()
pivoted = pivoted.rename({'m014':'Age 0 to 14', 'm1524':'Age 15 to 24'}, axis='columns')
print(pivoted.head())

# Add new comment
# Add another new comment
# Add another new comment
# Add comment
# Add another practice comment
# Added yet another practice comment
# Added comment on new branch practice 1