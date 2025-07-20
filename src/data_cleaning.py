

import pandas as pd

def load_data(file_path):
    """
    Load dataset from a specified file path.
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(df):
    """
    Cleans the data by handling missing values and converting categorical variables.
    """
    # Fill missing values for 'Item_Weight' with the mean
    df['Item_Weight'].fillna(df['Item_Weight'].mean(), inplace=True)
    
    # Fill missing values for 'Outlet_Size' with the mode
    df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0], inplace=True)
    
    return df

def map_categorical_columns(df):
    """
    Maps categorical columns to numerical values for model building.
    """
    # Mapping categorical columns
    df['Outlet_Location_Type'] = df['Outlet_Location_Type'].map({'Tier 1': 0, 'Tier 2': 1, 'Tier 3': 2})
    df['Outlet_Type'] = df['Outlet_Type'].map({'Supermarket Type1': 0, 'Supermarket Type2': 1, 'Supermarket Type3': 2, 'Grocery Store': 3})
    df['Outlet_Size'] = df['Outlet_Size'].map({'Small': 0, 'Medium': 1, 'High': 2})
    df['Item_Fat_Content'] = df['Item_Fat_Content'].map({'Low Fat': 0, 'Regular': 1})
    
    # Dropping unique identifier columns
    df.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)
    
    # Dropping unnecessary columns
    df.drop('Outlet_Establishment_Year', axis=1, inplace=True)
    
    return df
    