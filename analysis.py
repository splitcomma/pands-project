#Project task
# Author: Andras Csullog

# Write a program called analysis.py that:  
#     1. Outputs a summary of each variable to a single text file,  
#     2. Saves a histogram of each variable to png files, and  
#     3. Outputs a scatter plot of each pair of variables.  
#     4. Performs any other analysis you think is appropriate

import matplotlib.pyplot as plt    # creating the plots
import pandas as pd                # for reading the data file
import seaborn as sns
#import pandas as pd
#from matplotlib import pyplot as plot

# Reading the data file:
irisData = pd.read_csv('iris.csv')

#textFile = open ("summary.txt", "w")

#  Setting columns
# irisData.columns = ["SL" ,"SW","PL", "PW","Speices"]

#speices = irisData.iloc[: , -1]

#print(variety.unique())


#Defining scatter plot with x and y axis
#plot.scatter(irisData["SL"], irisData["SW"])

#x = irisData['SepalLengthCm']
#y = irisData['SepalWidthCm']

#x2 = irisData['PetalLengthCm']
#y2 = irisData['PetalWidthCm']

#plt.scatter(x , y, c = 'magenta')

sns.scatterplot(x = "SepalLengthCm" , y = "SepalWidthCm", data = irisData, hue = "Species", palette = ['green', 'red', 'blue'])
plt.show()
sns.scatterplot(x = "PetalLengthCm" , y = "PetalWidthCm", data = irisData, hue = "Species", palette = ['green', 'red', 'blue'])               
plt.show()




# References:
# https://en.wikipedia.org/wiki/Iris_flower_data_set

# https://stackoverflow.com/questions/27241253/print-the-unique-values-in-every-column-in-a-pandas-dataframe
# https://www.w3schools.com/python/matplotlib_scatter.asp
# https://datagy.io/python-matplotlib/
# https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
# https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
# https://python-graph-gallery.com/43-use-categorical-variable-to-color-scatterplot-seaborn
# https://saralgyaan.com/posts/matplotlib-tutorial-in-python-chapter-6-scatter-plotting/

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

# https://datagy.io/python-matplotlib/

# https://seaborn.pydata.org/tutorial/distributions.html
# https://seaborn.pydata.org/generated/seaborn.histplot.html
# https://medium.com/geekculture/python-seaborn-statistical-data-visualization-in-plot-graph-f149f7a27c6e
