import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn import linear_model
import pickle

data=pd.read_csv("student.csv")
print(data.head())
label_encoder=preprocessing.LabelEncoder()
data['Motivated And Confident']=label_encoder.fit_transform(data['Motivated And Confident'])
data['Motivated And Confident'].unique()
x=data.iloc[:,:-1].values
y=data.iloc[:,3].values

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1) 

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
pickle.dump(linear,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

acc = linear.score(x_test, y_test)
print(acc)