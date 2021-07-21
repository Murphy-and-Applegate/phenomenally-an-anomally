# This is Murphy and Applegate's Data Preparation Module for the Anomaly Detection Project

import pandas as pd
import requests
import numpy as np
from datetime import timedelta, datetime

def new_names(df):
    '''
    This function takes in the newly acquired curriculum logs and cohorts DataFrame, and renames columns to make them more user-friendly.
    '''
    
    df.rename(columns = {'name': 'cohort', 'path':'endpoint'}, inplace = True)
    
    return df

def program_feature(df):
    '''
    This function takes in the newly acquired curriculum logs and cohorts DataFrame, and creates a new column with cohort names.
    '''
    
    #creating new feature which gives name instead of number.
    df['program'] = df.program_id.replace([1,2,3,4], ['full_stack_php', 'java', 'data_science', 'front_end_program'])
    
    return df

def index_reset(df):
    '''
    This function will take in our newly acquired curriculum logs and cohorts DataFrame, and combine the 'date' and 'time' columns into one 'dt' column that will be set as the index
    '''
    
    # Concat 'date' and 'time' to 'dt'
    df['dt'] = df['date'] + ' ' + df['time']
    
    # Convert ot datetime
    df['dt'] = pd.to_datetime(df['dt'])
    
    # Set to index
    df = df.set_index(df['dt']).sort_index()
    
    return df

def make_time(df, col_list):
    '''
    This function takes in my curriculum logs and cohorts DataFrame, and a list of columns, and converts those columns to datetime. Then returns a pandas DataFrame.
    '''
    
    col_list = ['start_date', 'end_date', 'created_at', 'updated_at']
    
    for col in col_list:
        df[col] = pd.to_datetime(df[col])
        
    return df

def drop_cols(df, col_list):
    '''
    This function takes in the curriculum logs and cohorts DataFrame, and a list of columns, drops those columns, and returns a pandas DataFrame.
    '''
    
    col_list = ['deleted_at', 'date', 'time', 'dt']
    
    df = df.drop(columns=col_list)
    
    return df

def initial_prep(df):
    '''
    This function take in the newly acquire curriculum logs and cohorts DataFrame, and performs the index reset, make_time, and drop_cols functions. This accomplishes our prep goals for our first iteration through the DS pipeline.
    '''
    # Joins 'date' and 'time' as 'dt'
    # converts to datetime
    # resets as index
    df = index_reset(df)
    
    # Converts all 'date' columns to datetime
    col_list = ['start_date', 'end_date', 'created_at', 'updated_at']
    df = make_time(df, col_list)
    
    # drops unnecessary columns
    col_list = ['deleted_at', 'date', 'time', 'dt']
    df = drop_cols(df, col_list)
    
    # drops null values
    df = df.dropna()
    
    # change column names
    df = new_names(df)
    
    # create program names
    df = program_feature(df)
    
    # writes updated file to csv
    df.to_csv('first_iteration_table.csv')
    
    return df

################# 
    
   