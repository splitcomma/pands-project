#Project task
# Author: Andras Csullog

# Write a program called analysis.py that:  
#     1. Outputs a summary of each variable to a single text file,  
#     2. Saves a histogram of each variable to png files, and  
#     3. Outputs a scatter plot of each pair of variables.  
#     4. Performs any other analysis you think is appropriate

import matplotlib.pyplot as plt    # creating the plots
import pandas as pd                # for reading the data file

# Reading the data file:
irisData = pd.read_csv('iris.csv')

#  Setting columns
irisData.columns = ["Sepal length","Sepal width","Petal length", "Petal width","Variety"]

#Defining scatter plot with x and y axis
plt.scatter(irisData["Sepal length"], irisData["Sepal width"])

plt.title ("Sepal length and Sepal width")
plt.xlabel ("Sepal length")
plt.ylabel ("Sepal width")
plt.show()