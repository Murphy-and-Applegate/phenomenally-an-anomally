# This is our Data Exploration Module for Anomoly Detection

# Imports
import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, display_html



############### Question 2 Functions #############################
# Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?


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

def add_math(df):
    '''
    This functions takes in a pandas DataFrame after it has gone through q2_prep. It adds 'min', 'max', and 'range' columns and returns a pandas DataFrame that allows easy viewing of results for question 2, broken down by program. It also runs the add_zscore function.
    '''
    # adds 'min' and 'max' cols for 'count' and 'cohort'
    df_a = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['min']))
    df_b = pd.DataFrame(df.groupby(['endpoint'])['cohort'].agg(['min']))
    df_c = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['max']))
    df_d = pd.DataFrame(df.groupby(['endpoint'])['cohort'].agg(['max']))
    df_e = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['mean'])).round(2)
    df_f = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['sum']))
    
    # merges into 1 DataFrame
    df_ab = pd.merge(df_a, df_b, how='left', on='endpoint')
    df_cd = pd.merge(df_c, df_d, how='left', on='endpoint')
    df_ef = pd.merge(df_e, df_f, how='left', on='endpoint')
    df = pd.merge(df_ab, df_cd, how='left', on='endpoint')
    df = pd.merge(df, df_ef, how='left', on='endpoint')
    
    # adds a 'range' column
    df['range'] = df['max_x']-df['min_x']
    df = df[df['min_x']>10].sort_values(by='range', ascending=False)
    
    # add zscore
    df = add_zscore(df)
    
    return df

def add_zscore(df):
    
    z_scores = pd.Series((df['sum'] - df['mean']) / df['sum'].std()).round(4)
    df['zscore'] = z_scores
    
    df = df.sort_values(by='zscore', ascending=False)
        
    return df[df['zscore'] > 2.5]

############################ Question 6 Functions ########################################
# What topics are grads continuing to reference after graduation and into their jobs (for each program)?

# Reacquire data
# Redo initial_prep
# Use remove_home function from q2
# Remove all entries where 'end_date' > index
# Use split_by_program function from q2
# Create q3_cols function that keeps 'index', 'cohort', 'endpoint', 'end_date', 'program_id'

# Split into 4 DataFrames, 1 for each program


def q6_cols(df):
    '''
    This function takes in the result of my remove_home function, and returns a pandas DataFrame with 'endpoint', 'cohort', 'end_date', and 'program_id' as columns. All other variables are dropped since they are not needed for question 6.
    '''
    
    df = df[['endpoint', 'cohort', 'end_date', 'program_id']]
    
    return df

def grads_only(df):
    '''
    This function takes in the result of my q6_cols function, and only returns data where the index > end_date, (which means student has graduated.)
    '''
    
    df = df[df.index > df.end_date]
    
    return df

def add_mm_range_mean(df):
    '''
    This functions takes in a pandas DataFrame after it has gone through q2_prep. It adds 'min', 'max', and 'range' columns and returns a pandas DataFrame that allows easy viewing of results for question 2, broken down by program.
    '''
    # adds 'min' and 'max' cols for 'count' and 'cohort'
    df_a = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['min']))
    df_b = pd.DataFrame(df.groupby(['endpoint'])['cohort'].agg(['min']))
    df_c = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['max']))
    df_d = pd.DataFrame(df.groupby(['endpoint'])['cohort'].agg(['max']))
    df_e = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['mean'])).round(2)
    df_f = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['sum']))
    
    # merges into 1 DataFrame
    df_ab = pd.merge(df_a, df_b, how='left', on='endpoint')
    df_cd = pd.merge(df_c, df_d, how='left', on='endpoint')
    df = pd.merge(df_ab, df_cd, how='left', on='endpoint')
    df = pd.merge(df, df_e, how='left', on='endpoint')
    df = pd.merge(df, df_f, how='left', on='endpoint')
    
    # adds a 'range' column
    df['range'] = df['max_x']-df['min_x']
    df = df.sort_values(by='range', ascending=False)
    
    # rename columns
    df = df.rename(columns={'min_x': 'min_count', 'min_y': 'min_cohort', 'max_x': 'max_count', 'max_y': 'max_cohort'})
    
    return df

def q6_math(df):
    '''
    This functions takes in a pandas DataFrame after it has gone through q6_prep. It adds 'min', 'max', 'sum', and 'range' columns and returns a pandas DataFrame that allows easy viewing of results for question 2, broken down by program.
    '''
    # adds 'min' and 'max' cols for 'count' and 'cohort'
    df_a = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['min']))
    df_b = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['max']))
    df_c = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['mean'])).round(2)
    df_d = pd.DataFrame(df.groupby(['endpoint'])['count'].agg(['sum']))
    
    # merges into 1 DataFrame
    df_ab = pd.merge(df_a, df_b, how='left', on='endpoint')
    df_cd = pd.merge(df_c, df_d, how='left', on='endpoint')
    df = pd.merge(df_ab, df_cd, how='left', on='endpoint')
    
    # adds a 'range' column
    df['range'] = df['max']-df['min']
    df = df.sort_values(by='range', ascending=False)
    
    # rename columns
#     df = df.rename(columns={'min_x': 'min_count', 'max_x': 'max_count'})
    
    return df



    
    













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