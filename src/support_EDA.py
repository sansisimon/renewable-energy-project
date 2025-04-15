import pandas as pd 

def pivot_df(df, original_cols, new_col, new_value):
    '''
    Transforms a DataFrame from wide format to long format using pd.melt.

    Parameters
    ----------
    df : pd.DataFrame
        The original DataFrame to be pivoted.

    original_cols : list of str
        List of column names to keep fixed (identifiers).

    new_col : str
        Name of the new column that will contain the original column names (variable name).

    new_value : str
        Name of the new column that will contain the values from the original columns.

    Returns
    -------
    pd.DataFrame
        Transformed DataFrame in long format, ideal for analysis or visualization.
    '''
    
    df_modified = df.melt(id_vars= original_cols, var_name= new_col, value_name= new_value)
    
    return df_modified