# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
temp_data = pd.read_csv("Platinum - Sheet1.csv", header=0)   # identify the header row

# TODO #2: Use matplotlib to make a line graph
plt.plot(temp_data['Year'], temp_data['Price'], color='gray')
plt.ylabel('$')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

# TODO #3: Plot LOWESS in a line graph
'''
plt.plot(temp_data['Year'], temp_data['LOWESS'], color='blue')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()
This and \|/ that are the same thing
'''
plt.plot(temp_data['Year'], temp_data['Price'], color='blue')
plt.show()
# TODO #4: Use matplotlib to make a bar chart
import matplotlib.pyplot as plt
import numpy as nu
plt.bar(temp_data['Year'], temp_data['Price'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()



# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
#hist2d
min_Price = temp_data['Price'][0]
max_Price = temp_data['Price'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_Price = 0
avg_Price = 0
# find the min, max and calculate the sum
for i in range(len(temp_data['Price'])):
  if (temp_data['Price'][i] < min_Price):
    min_Price = temp_data['Price'][i]
    min_year = temp_data['Year'][i]
  # new code inside the same for loop
  
  if (temp_data['Price'][i] > max_Price):
    max_Price = temp_data['Price'][i]
    max_Price = temp_data['Year'][i]
  sum_Price = sum_Price + temp_data['Price'][i]

avg_Price = sum_Price/len(temp_data['Price'])

#print the statistical values
print("The maximum anomaly is:", max_Price, "which occured in", max_year)

print("The minimum anomaly is:", min_Price, "which occured in", min_year)

print("The average anomaly is:", avg_Price)
