# Fisher’s Iris Data Set project

## Problem statement

This project concerns the well-known Fisher’s Iris data set It is a research of the data set, inclluding documentation and code .

The program file called analysis.ipynb does: 

1. Outputs a summary of each variable to a single text file,  
2. Saves a histogram of each variable to png files, and  
3. Outputs a scatter plot of each pair of variables.

## Background

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper. 

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). 
![3 Iris Species](https://github.com/splitcomma/pands-project/blob/main/images/iris_classes.png)

Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

## Summary output


```

 **********   Summary of the Iris Data set and its variables  **********   

              Heading the first 5 lines of the Iris Data
---------------------------------------------------------------------------
   SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0            5.1           3.5            1.4           0.2  Iris-setosa
1            4.9           3.0            1.4           0.2  Iris-setosa
2            4.7           3.2            1.3           0.2  Iris-setosa
3            4.6           3.1            1.5           0.2  Iris-setosa
4            5.0           3.6            1.4           0.2  Iris-setosa
---------------------------------------------------------------------------
                    Sum the Iris Data
---------------------------------------------------------------------------
SepalLengthCm                                                876.5
SepalWidthCm                                                 458.1
PetalLengthCm                                                563.8
PetalWidthCm                                                 179.8
Species          Iris-setosaIris-setosaIris-setosaIris-setosaIr...
dtype: object
---------------------------------------------------------------------------
                    Covariance matrix of the Iris Data
---------------------------------------------------------------------------
               SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
SepalLengthCm       0.685694     -0.039268       1.273682      0.516904
SepalWidthCm       -0.039268      0.188004      -0.321713     -0.117981
PetalLengthCm       1.273682     -0.321713       3.113179      1.296387
PetalWidthCm        0.516904     -0.117981       1.296387      0.582414
---------------------------------------------------------------------------
                      Ranking Iris Data
---------------------------------------------------------------------------
               SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
SepalLengthCm       0.685694     -0.039268       1.273682      0.516904
SepalWidthCm       -0.039268      0.188004      -0.321713     -0.117981
PetalLengthCm       1.273682     -0.321713       3.113179      1.296387
PetalWidthCm        0.516904     -0.117981       1.296387      0.582414
---------------------------------------------------------------------------
                      Correlation Iris Data
---------------------------------------------------------------------------
               SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
SepalLengthCm       1.000000     -0.109369       0.871754      0.817954
SepalWidthCm       -0.109369      1.000000      -0.420516     -0.356544
PetalLengthCm       0.871754     -0.420516       1.000000      0.962757
PetalWidthCm        0.817954     -0.356544       0.962757      1.000000
---------------------------------------------------------------------------
                    Summarizing the Iris Data
---------------------------------------------------------------------------
       SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count     150.000000    150.000000     150.000000    150.000000
mean        5.843333      3.054000       3.758667      1.198667
std         0.828066      0.433594       1.764420      0.763161
min         4.300000      2.000000       1.000000      0.100000
25%         5.100000      2.800000       1.600000      0.300000
50%         5.800000      3.000000       4.350000      1.300000
75%         6.400000      3.300000       5.100000      1.800000
max         7.900000      4.400000       6.900000      2.500000
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
                    Shape the Iris Data
---------------------------------------------------------------------------
(150, 5)
---------------------------------------------------------------------------
              Printing the last 5 rows Iris Data
---------------------------------------------------------------------------
     SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
145            6.7           3.0            5.2           2.3  Iris-virginica
146            6.3           2.5            5.0           1.9  Iris-virginica
147            6.5           3.0            5.2           2.0  Iris-virginica
148            6.2           3.4            5.4           2.3  Iris-virginica
149            5.9           3.0            5.1           1.8  Iris-virginica
```

## Histogram

![Histogram](https://github.com/splitcomma/pands-project/blob/main/images/histogram.png)

## Plots

### Scatter Plot

![Scatter](https://github.com/splitcomma/pands-project/blob/main/images/scatter_plot.png)

### Joint Plot

![Joint](https://github.com/splitcomma/pands-project/blob/main/images/joint_plot.png)

### Swarm Plot

![Swarm](https://github.com/splitcomma/pands-project/blob/main/images/swarm_plot.png)

### Pair Plot

![Pair](https://github.com/splitcomma/pands-project/blob/main/images/pair_plot.png)

### Distribution Plot

![Distribution](https://github.com/splitcomma/pands-project/blob/main/images/distribution_plot.png)


## Usage:

### Preprequisities in Windows:
Git, Python, Anaconda, Jupyter installed

### Libraries needed and installed:
```
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt 
```    

Run in  cmd:
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
