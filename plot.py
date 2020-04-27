import pandas as pd
import matplotlib.pyplot as plt
def scatter(pred):
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    empsal_df = pd.read_csv('Dataset/empsal.csv', index_col='empno', parse_dates=['dob'])
    empsal_df.dropna(axis=0, how='any', inplace=True)       

    x = empsal_df.iloc[:, -3].values
    y = empsal_df.iloc[:, -2].values 
    x = x.reshape(-1,1)
    
    # Draw a scatter plot of Experience vs. Salary
    plt.scatter(x,y, color = 'red', label='Salary')
    plt.plot(x, pred.predict(x), color = 'blue',label='Prediction')
    plt.title('Salary vs Experience\nScatter Plot')
    plt.xlabel('Years of Experience-->')
    plt.ylabel('Salary-->')
    plt.show()













