#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


def run_sql_query(query, conn):
    """
    Executes the SQL query on the provided SQLite connection.
    """
    try:
        result = pd.read_sql_query(query, conn)
        return result
    except Exception as e:
        return f"Error running SQL query: {e}"

