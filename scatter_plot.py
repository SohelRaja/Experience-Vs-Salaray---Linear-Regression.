import pandas as pd
import matplotlib.pyplot as plt

def scatterPlot():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    empsal_df = pd.read_csv('DataSet/empsal.csv', index_col='empno', parse_dates=['dob'])
    empsal_df.dropna(axis=0, how='any', inplace=True)       

    expyr = empsal_df['expyr']
    salary = empsal_df['salary']

    # Draw a scatter plot of Experience vs. Salary
    plt.scatter(expyr, salary, color = 'red', label='Salary')
    plt.title('Salary vs Experience\nScatter Plot')
    plt.xlabel('Years of Experience-->')
    plt.ylabel('Salary-->')
    plt.show()












