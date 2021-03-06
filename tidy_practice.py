# Import all packages
# export PATH="/usr/local/opt/python/libexec/bin:$PATH"
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import scipy.io 

# Import url for table
from urllib.request import urlretrieve
url = 'https://assets.datacamp.com/production/course_2023/datasets/tb.csv'
# urlretrieve(url, 'tb.csv')

df = pd.read_csv(url, sep=',')
print(df.head())

# Melt age columns from 0 to 44, then pivot to split
melted = pd.melt(df, id_vars = ['country', 'year'], value_vars = ['m014', 'm1524', 'm2534', 'm3544'], value_name = 'value')

# Print melted table
print(melted.head())

# Pivot table on variable column and create new 'sex' column
melted['sex'] = melted.variable.str[0]
print(melted.head())

pivot = melted.pivot_table(values = 'value', index = ['country', 'year'], columns = 'variable', aggfunc = np.mean).reset_index()
pivot = pivot.rename({'m014':'0 to 14', 'm1524':'15 to 24', 'm2534':'25 to 34', 'm3544':'35 to 44'}, axis = 1)
print(pivot.head())

# # Melt age and sex columns into new table
# melted = pd.melt(df, id_vars = ['country', 'year'], value_vars = ['m014', 'm1524'], value_name = 'value')
# print(melted.head())

# # Create new column for sex using string value from variable
# melted['sex'] = melted.variable[0][0]

# # Pivot table on m014 and m1524
# pivoted = melted.pivot_table(values = 'value', index = ['country', 'year', 'sex'], columns = 'variable', aggfunc = np.mean)
# pivoted = pivoted.reset_index()
# pivoted = pivoted.rename({'m014':'Age 0 to 14', 'm1524':'Age 15 to 24'}, axis='columns')
# print(pivoted.head())
