import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# import codecademylib3_seaborn 
import os

## add code below
## read in csv file
print('Current directory =', os.getcwd()) # Print the current working directory
cars = pd.read_csv('Misc/cars.csv')

## set you price variable
prices = cars['sellingprice']
print(prices.head())

## plot a histogram of prices
plt.hist(prices, bins = 150)
plt.xticks(rotation = 45)
plt.title('Prices of Cars')
plt.ylabel('Number of Cars')
plt.xlabel('Price')
plt.show()

## log transform prices
log_prices = np.log(prices)
print(log_prices.head())

## plot a histogram of log_prices
plt.hist(log_prices, bins = 150)
plt.xticks(rotation = 45)
plt.title('Log-Prices of Cars')
plt.ylabel('Number of Cars')
plt.xlabel('Log-Price')
plt.show()
