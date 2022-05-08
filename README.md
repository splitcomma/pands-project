# Fisher’s Iris Data Set project

## Problem statement

This project concerns the well-known Fisher’s Iris data set It is a research of the data set, inclluding documentation and code .

The program file called **analysis.ipynb** does: 

1. Outputs a summary of each variable to a single text file,  
2. Saves histogram of each variable to png files, and  
3. Outputs a scatter plot of each pair of variables,
4. Plus other plots and analysis.

## Background

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper. 

The data set consists of 50 samples from each of three species of Iris: Iris setosa, Iris virginica and Iris versicolor.
![3 Iris Species](https://github.com/splitcomma/pands-project/blob/main/images/iris_classes.png)

Four features were measured from each sample: the **length** and the **width** of the **sepals** and **petals**, in centimeters.

## About the data and visualization

We have a relatively small data set consisting 150 lines on three different species of Iris flowers 50/50/50 lines of each.
Each line of data consist of 4 measurements that can be grouped by length and width of Petal and Sepal parts of each flower.
It is worthwhile mentioning that only two of the species were collected on the same island and pasture.
I have failed to find more details on the collection methodology and although the above mentioned two species where collected on the same land, there is no indication of time as a dimension.

### Summary output

Familiarizing with the data set printing out the top 5 lines, results of sum the Iris data lead to no significant conclusion.
By displaying covariance and correlation, attempted to see if petal and sepal length figures are moving together among the three species and the strength of relationship between the two variables, receiving mixed covariance (negative/positive) with weak correlation.

Summarizing the Iris data section first calculated basic statistical expressions such as min/max/mean/standard deviation. First section on the entire data set and underneath for each species supporting easier comparison. Iris Setosa has the lowest mean, standard deviation and min/max values when Sepal width is examined.

```
**********   Summary of the Iris Data set and its variables  **********   

              Heading the first 5 lines of the Iris Data
---------------------------------------------------------------------------
   SepalLength_Cm  SepalWidth_Cm  PetalLength_Cm  PetalWidth_Cm      Species
0             5.1            3.5             1.4            0.2  Iris-setosa
1             4.9            3.0             1.4            0.2  Iris-setosa
2             4.7            3.2             1.3            0.2  Iris-setosa
3             4.6            3.1             1.5            0.2  Iris-setosa
4             5.0            3.6             1.4            0.2  Iris-setosa
---------------------------------------------------------------------------
                    Sum the Iris Data
---------------------------------------------------------------------------
SepalLength_Cm                                                876.5
SepalWidth_Cm                                                 458.1
PetalLength_Cm                                                563.8
PetalWidth_Cm                                                 179.8
Species           Iris-setosaIris-setosaIris-setosaIris-setosaIr...
dtype: object
---------------------------------------------------------------------------
                    Covariance matrix of the Iris Data
---------------------------------------------------------------------------
                SepalLength_Cm  SepalWidth_Cm  PetalLength_Cm  PetalWidth_Cm
SepalLength_Cm        0.685694      -0.039268        1.273682       0.516904
SepalWidth_Cm        -0.039268       0.188004       -0.321713      -0.117981
PetalLength_Cm        1.273682      -0.321713        3.113179       1.296387
PetalWidth_Cm         0.516904      -0.117981        1.296387       0.582414
---------------------------------------------------------------------------
                      Correlation Iris Data
---------------------------------------------------------------------------
                SepalLength_Cm  SepalWidth_Cm  PetalLength_Cm  PetalWidth_Cm
SepalLength_Cm        1.000000      -0.109369        0.871754       0.817954
SepalWidth_Cm        -0.109369       1.000000       -0.420516      -0.356544
PetalLength_Cm        0.871754      -0.420516        1.000000       0.962757
PetalWidth_Cm         0.817954      -0.356544        0.962757       1.000000
---------------------------------------------------------------------------
                    Summarizing the Iris Data
---------------------------------------------------------------------------
       SepalLength_Cm  SepalWidth_Cm  PetalLength_Cm  PetalWidth_Cm
count      150.000000     150.000000      150.000000     150.000000
mean         5.843333       3.054000        3.758667       1.198667
std          0.828066       0.433594        1.764420       0.763161
min          4.300000       2.000000        1.000000       0.100000
25%          5.100000       2.800000        1.600000       0.300000
50%          5.800000       3.000000        4.350000       1.300000
75%          6.400000       3.300000        5.100000       1.800000
max          7.900000       4.400000        6.900000       2.500000
---------------------------------------------------------------------------
                    Summarizing the Iris Data
---------------------------------------------------------------------------
                SepalLength_Cm                                              \
                         count   mean       std  min    25%  50%  75%  max   
Species                                                                      
Iris-setosa               50.0  5.006  0.352490  4.3  4.800  5.0  5.2  5.8   
Iris-versicolor           50.0  5.936  0.516171  4.9  5.600  5.9  6.3  7.0   
Iris-virginica            50.0  6.588  0.635880  4.9  6.225  6.5  6.9  7.9   

                SepalWidth_Cm         ... PetalLength_Cm      PetalWidth_Cm  \
                        count   mean  ...            75%  max         count   
Species                               ...                                     
Iris-setosa              50.0  3.418  ...          1.575  1.9          50.0   
Iris-versicolor          50.0  2.770  ...          4.600  5.1          50.0   
Iris-virginica           50.0  2.974  ...          5.875  6.9          50.0   

                                                           
                  mean       std  min  25%  50%  75%  max  
Species                                                    
Iris-setosa      0.244  0.107210  0.1  0.2  0.2  0.3  0.6  
Iris-versicolor  1.326  0.197753  1.0  1.2  1.3  1.5  1.8  
Iris-virginica   2.026  0.274650  1.4  1.8  2.0  2.3  2.5  

[3 rows x 32 columns]
---------------------------------------------------------------------------
                    Duplicates the Iris Data
---------------------------------------------------------------------------
0      False
1      False
2      False
3      False
4      False
       ...  
145    False
146    False
147    False
148    False
149    False
Length: 150, dtype: bool
---------------------------------------------------------------------------
                    Number of rows and columns the Iris Data
---------------------------------------------------------------------------
(150, 5)
---------------------------------------------------------------------------
              Printing the last 5 rows Iris Data
---------------------------------------------------------------------------
     SepalLength_Cm  SepalWidth_Cm  PetalLength_Cm  PetalWidth_Cm  \
145             6.7            3.0             5.2            2.3   
146             6.3            2.5             5.0            1.9   
147             6.5            3.0             5.2            2.0   
148             6.2            3.4             5.4            2.3   
149             5.9            3.0             5.1            1.8   

            Species  
145  Iris-virginica  
146  Iris-virginica  
147  Iris-virginica  
148  Iris-virginica  
149  Iris-virginica  
---------------------

```
## Plots:

### Histograms

Histograms to visualize spread of Sepal length among the three species. Columns to indicate y axis the count of occurrence in the data set for centimeter values.
Iris Setosa shows a low standard deviation and significantly shorter length compared to Versicolor and Virginica.

![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/histogram.png)

Sepal and Petal ratio created as a quantitative relationship between Sepal length/Sepal width and for Petal Length / Petal width. The two histograms are showing significant difference between the ratios for Setosa. Unique characteristics on standard deviation that is adverse for Sepal and Petal ratio.

![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/histogram1.png)
![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/histogram2.png)
![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/histogram3.png)
![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/histogram4.png)

Seaborn histplot was an experiment that did not bring me closer to relevant conclusions.

![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/hist_plot.png)

Underneath similar experiment to utilize newly learnt statistical expression "kernel density estimation (KDE) is a non-parametric way to estimate the probability density".

![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/hist_plot2.png)


### Scatter Plot

Observations based on the scatterplots follows:

On Sepal length among the three species 
While Setosa has smaller length but a greater width, Virginica shows opposite features to Setosa.
 
On Petal length among the three species 
Setosa has significantly smaller length and width compared to the other two species. Versicolor and Virginica are much closer on this aspect with the latter taking the lead.

![Scatter](https://github.com/splitcomma/pands-project/blob/main/images/scatter_plot.png)
![Scatter](https://github.com/splitcomma/pands-project/blob/main/images/scatter_plot2.png)
![Scatter](https://github.com/splitcomma/pands-project/blob/main/images/scatter_plot3.png)
![Scatter](https://github.com/splitcomma/pands-project/blob/main/images/scatter_plot4.png)

![Scatter](https://github.com/splitcomma/pands-project/blob/main/images/striplot.png)

### Joint Plot

Joint plot added as an experiment, output in current format looks visually very intriguing but single color condensing all three species carries low amount of information to help better understand our data.

![Joint](https://github.com/splitcomma/pands-project/blob/main/images/joint_plot.png)

### Pair Plot

Pair plot turned out to be a very easy to use plotting method that auto generated almost all my scatter and histplots in a quick and compact matrix format.

![Pair](https://github.com/splitcomma/pands-project/blob/main/images/pair_plot.png)


## Usage of the project:

### Preprequisities in Windows:
Git, Python, Anaconda, Jupyter installed

### Libraries needed and installed:
```
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt 
```    

Run in Command Prompt:
```
git clone https://github.com/splitcomma/pands-project.git
```

Run in anaconda cmd:
```
cd pands-project
```
```
jupyter analysis.ipynb
```

## References
- https://en.wikipedia.org/wiki/Iris_flower_data_set
- https://archive.ics.uci.edu/ml/datasets/iris
- https://stackoverflow.com/questions/27241253/print-the-unique-values-in-every-column-in-a-pandas-dataframe
- https://www.w3schools.com/python/matplotlib_scatter.asp
- https://datagy.io/python-matplotlib/
- https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
- https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
- https://python-graph-gallery.com/43-use-categorical-variable-to-color-scatterplot-seaborn
- https://saralgyaan.com/posts/matplotlib-tutorial-in-python-chapter-6-scatter-plotting/
- https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
- https://datagy.io/python-matplotlib/
- https://seaborn.pydata.org/tutorial/distributions.html
- https://seaborn.pydata.org/generated/seaborn.histplot.html
- https://medium.com/geekculture/python-seaborn-statistical-data-visualization-in-plot-graph-f149f7a27c6e
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/


