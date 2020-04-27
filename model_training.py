#importing the required modules
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#importing the data
import transferFile
data = transferFile.file_import()

def train():
    #reading the data to empsal_df
    empsal_df = pd.read_csv(data)

    #print(empsal_df.columns)
    #initializing x and y
    x = empsal_df.iloc[:, -3].values
    y = empsal_df.iloc[:, -2].values 

    #converting the x into 2D 
    x = x.reshape(-1,1)

    # Splitting the Dataset into Training Set and Test Set
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

    #creating the model
    model = LinearRegression()

    #fitting the data to model
    model.fit(X_train, y_train)

    # Predicting the Test Set Results
    y_pred = model.predict(X_test)

    #calculating the accuracy of the model
    acc = model.score(X_test,y_test)

    #calculating the intercept and coefficient
    intercept = model.intercept_
    coef = model.coef_

    #predicting the unknown salary
    unknown_salary = model.predict([[9]])

    #print(acc,intercept,coef,unknown_salary)
    return [model,acc,intercept,coef]

