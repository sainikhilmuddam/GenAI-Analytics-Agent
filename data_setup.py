#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import sqlite3


# In[ ]:


def read_csvs_from_directory(directory_path):
    """
    Reads all CSV files in the given directory and returns a dict of DataFrames.
    """
    dataframes = {}
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            path = os.path.join(directory_path, filename)
            df_name = os.path.splitext(filename)[0]
            dataframes[df_name] = pd.read_csv(path)
    return dataframes


# In[ ]:


def create_sqlite_db_from_dfs(dataframes):
    """
    Creates an in-memory SQLite database from the provided DataFrames.
    """
    conn = sqlite3.connect(":memory:")
    for table_name, df in dataframes.items():
        df.to_sql(table_name, conn, index=False, if_exists='replace')
    return conn


# In[ ]:


def get_metadata_from_dfs(dataframes):
    """
    Extracts schema metadata from the DataFrames for LLM prompting.
    """
    metadata_list = []
    for table_name, df in dataframes.items():
        cols = [f"- {col} ({str(dtype)})" for col, dtype in df.dtypes.items()]
        metadata = f"Table: {table_name}\nColumns:\n" + "\n".join(cols)
        metadata_list.append(metadata)
    return "\n\n".join(metadata_list)

