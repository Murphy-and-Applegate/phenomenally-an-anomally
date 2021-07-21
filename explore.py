# This is our Data Exploration Module for Anomoly Detection

# Imports
import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, display_html



############### General Exploration Functions #############################

def split_by_program(df):
    '''
    This functions takes in my prepped cohorts and curriculum logs DataFrame and returns a separate DataFrame for each program.
    '''
    
    df_1 = df[df['program_id'] ==1]
    df_2 = df[df['program_id'] ==2]
    df_3 = df[df['program_id'] ==3]
    df_4 = df[df['program_id'] ==4]
    
    return df_1, df_2, df_3, df_4












############## Child Functions for IQR / Outliers ###########################

        
def get_plot_iqr_stats(df, col, k=1.5):
    '''
    This function will take in a pandas Series and plot a histogram and boxplot, with whiskers set based on value of k.
    '''
    
    # Find the lower and upper quartiles
    q_25, q_75 = df[col].quantile([0.25, 0.75])
    # Find the Inner Quartile Range
    q_iqr = q_75 - q_25
    # Find the Upper Bound
    q_upper = q_75 + (k * q_iqr)
    # Find the Lower Bound
    q_lower = q_25 - (k * q_iqr)
    # Identify outliers
    outliers_lower = df[df[col] < q_lower]
    outliers_upper = df[df[col] > q_upper]
    outliers_all = pd.concat([outliers_lower, outliers_upper], axis=0)
    
    print(f'''
{col}

K: {k}
IQR: {q_iqr}
Lower Fence: {q_lower}
Upper Fence: {q_upper}
''')
    print(f'{col} Lower Outliers')
    display(outliers_lower)
    print(f'{col} Upper Outliers')
    display(outliers_upper)
    print(f'{col} All Outliers')
    display(outliers_all)
    
    plt.figure(figsize=(16,4))
    plt.subplot(1, 2, 1)
    sns.histplot(data = df, x = col, kde=True)
    plt.axvline(x = q_lower, color = 'orange')
    plt.axvline(x = q_upper, color= 'orange')
    plt.title(col)
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col], data=df, whis=k)
    plt.title(col)
    plt.show()

        


def whole_df_iqr(df, k=1.5):
    col_list = list(df.select_dtypes(include=['int', 'float'], exclude='O'))
    
    for col in col_list:
        get_plot_iqr_stats(df, col, k=k)
        
    return df.info()