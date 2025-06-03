#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import google.generativeai as genai


# In[ ]:


# Configure your API key (set this at runtime)
def configure_llm(api_key, model_name="gemini-1.5-flash-latest"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)


# In[ ]:


def generate_sql_query(question, metadata, model):
    """
    Prompts the LLM to generate a SQL query based on schema metadata and user question.
    """
    prompt = (
        f"You are an expert data analyst. Based on the following table schemas:\n\n"
        f"{metadata}\n\n"
        f"Write a syntactically correct SQL query (MySQL) for this question:\n"
        f"{question}\n"
        f"Give the query only, nothing else.\n"
        f"When calculating ratios in SQL, multiply the numerator by 1.0 or use CAST(... AS FLOAT) to force float division.\n"
        f"When giving the final result, always order it in a way you see fit."
    )
    response = model.generate_content(prompt)
    return response.text.strip("`sql\n").strip("`")

