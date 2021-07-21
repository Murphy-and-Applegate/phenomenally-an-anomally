# This is our Data Exploration Module for Anomoly Detection

# Imports
import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, display_html



############### Question 2 Functions #############################

def remove_home(df):
    '''
    This function take in my prepped cohorts and curriculum logs DataFrame and removes all 'endpoint' that are '/', which is the homepage, and not an actual lesson.
    '''
    df = df[df['endpoint'] != '/']
    
    return df

def q2_cols(df):
    '''
    This function takes in the result of my remove_home function, and returns a pandas DataFrame with 'endpoint', 'cohort', and 'program_id' as columns. All other variables are dropped since they are not needed for question 2.
    '''
    
    df = df[['endpoint', 'cohort', 'program_id']]
    
    return df

def split_by_program(df):
    '''
    This functions takes in my prepped cohorts and curriculum logs DataFrame and returns a separate DataFrame for each program.
    '''
    
    df_1 = df[df['program_id'] ==1].drop(columns = 'program_id')
    df_2 = df[df['program_id'] ==2].drop(columns = 'program_id')
    df_3 = df[df['program_id'] ==3].drop(columns = 'program_id')
    df_4 = df[df['program_id'] ==4].drop(columns = 'program_id')
    
    return df_1, df_2, df_3, df_4

def endpoint_group(df_1, df_2, df_3, df_4):
    '''
    This function takes in my 4 pandas DataFrames split by program_id, and returns 
    '''
    
    # Groupby 'endpoint' and get value counts for 'cohort'
    # Create a 'count' column
    df_1 = pd.DataFrame(df_1.groupby('endpoint')['cohort'].value_counts()).rename(columns = {'cohort':'count'})
    df_2 = pd.DataFrame(df_2.groupby('endpoint')['cohort'].value_counts()).rename(columns = {'cohort':'count'})
    df_3 = pd.DataFrame(df_3.groupby('endpoint')['cohort'].value_counts()).rename(columns = {'cohort':'count'})
    df_4 = pd.DataFrame(df_4.groupby('endpoint')['cohort'].value_counts()).rename(columns = {'cohort':'count'})
    
    # Unstack the multi-level index, to return useable DataFrames
    df_1 = df_1.reset_index(level=['endpoint', 'cohort'])
    df_2 = df_2.reset_index(level=['endpoint', 'cohort'])
    df_3 = df_3.reset_index(level=['endpoint', 'cohort'])
    df_4 = df_4.reset_index(level=['endpoint', 'cohort'])
    
    return df_1, df_2, df_3, df_4

def q2_prep(df):
    '''
    This functions combines all of my question 2 functions, and returns 4 pandas DataFrames ready to be explored in order to answer question 2.
    '''
    
    # remove the '/' 'endpoint'
    df = remove_home(df)
    
    # drop down to only necessary columns for question 2
    df = q2_cols(df)
    
    # split into 4 pandas DataFrames, 1 for each program_id
    df_1, df_2, df_3, df_4 = split_by_program(df)
    
    # give valueable tables for exploration grouped by 'endpoint'
    df_1, df_2, df_3, df_4 = endpoint_group(df_1, df_2, df_3, df_4)
    
    return df_1, df_2, df_3, df_4

def add_mm_range(df):
    '''
    This functions takes in a pandas DataFrame after it has gone through q2_prep. It adds 'min', 'max', and 'range' columns and returns a pandas DataFrame that allows easy viewing of results for question 2, broken down by program.
    '''
    # adds 'min' and 'max' cols for 'count' and 'cohort'
    df_a = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['min']))
    df_b = pd.DataFrame(df.groupby(['endpoint'])['cohort'].agg(['min']))
    df_c = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['max']))
    df_d = pd.DataFrame(df.groupby(['endpoint'])['cohort'].agg(['max']))
    
    # merges into 1 DataFrame
    df_ab = pd.merge(df_a, df_b, how='left', on='endpoint')
    df_cd = pd.merge(df_c, df_d, how='left', on='endpoint')
    df = pd.merge(df_ab, df_cd, how='left', on='endpoint')
    
    # adds a 'range' column
    df['range'] = df['max_x']-df['min_x']
    df = df[df['min_x']>10].sort_values(by='range', ascending=False)
    
    return df

############################ Question 6 Functions ########################################

# Use remove_home function from q2
# Use split_by_program function from q2

    
    













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