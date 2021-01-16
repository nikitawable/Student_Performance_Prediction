<h1 align="center">Student Performance Visualizer and Predictor</h1> 

<p align="center">
A machine learning model to predict and visualize student performances in school based on several attributes. I was able to get the accuracy of this model to about 92%. </p>

<p align="center">
The data I used to train the model can be found here: <a href="https://archive.ics.uci.edu/ml/datasets/Student+Performance" target="_blank">archive.ics.uci.edu/ml/datasets/Student+Performance</a>
</p>

## Repository Contents
* [studentPerformance.ipynb](https://github.com/aahmad4/Student-Performance-Visualizer-and-Predictor/blob/master/studentPerformance.ipynb) contains the Python code for this model. I have commented all the logic going on so it's easier to understand and follow. I also have graphs with matplotlib to visualize the data and see the correlation between the label and it's attributes. 
* Along with my notebook, I have two csv files which contain the data for students performances based on all 33 attributes. 
* [student.txt](https://github.com/aahmad4/Student-Performance-Visualizer-and-Predictor/blob/master/student.txt) contains all the attributes and the number/string values associated with them.
* [student_model.pickle](https://github.com/aahmad4/Student-Performance-Visualizer-and-Predictor/blob/master/student_model.pickle) is a pickle file I made in my Python program to store the model with my highest accuracy. 

## Linear Regression Examples

![](screenshot1.png)     ![](screenshot2.png)

## Setup

#### Clone
```
git clone https://github.com/aahmad4/Student-Performance-Visualizer-and-Predictor
```

#### Usage
```
cd Student-Performance-Visualizer-and-Predictor
```
```
jupyter notebook
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
