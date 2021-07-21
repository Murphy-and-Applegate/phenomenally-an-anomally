# This is Murphy and Applegate's Data Acquistion Module for our Anomaly Detection Project

import pandas as pd
import numpy as np
import os
from env import host, user, password

############################## general framework / template ###############################
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_cohort_curr_data():
    '''
    This function uses my credentials to connect to the Codeup database. It joins the cohorts and logs tables from the curriculum_logs dataset.
    '''

    sql_query = '''
                SELECT *
                FROM logs
                JOIN cohorts
                ON logs.cohort_id = cohorts.id
                '''
    
    return pd.read_sql(sql_query, get_connection('curriculum_logs'))


def get_cohort_curr_data():
    '''
    This function first looks locally for a stored csv file of my merged cohorts and curriculum logs data. If one is not found, then it runs the new_cohort_curr_data function to connect to the Codeup database and pull both tables from the curriculum logs dataframe.
    '''

    if os.path.isfile('cohort_curr.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('cohort_curr.csv', index_col=0)
        
    else:
        # Read fresh data from db into a DataFrame
        df = new_cohort_curr_data()
        # Cache data
        df.to_csv('cohort_curr.csv')

    return df

###################