#!/usr/bin/env python
# coding: utf-8

# In[23]:


import openai
import os


# In[24]:





# In[25]:


openai.api_key = os.getenv("API_KEY")


# In[26]:


pip install pandas


# In[27]:


import pandas as pd


# In[28]:


df = pd.read_csv("sales_data_sample.csv")


# In[29]:


df


# In[30]:


pip install sqlalchemy


# In[31]:


import sqlalchemy


# In[32]:


from sqlalchemy import create_engine
from sqlalchemy import text


# In[33]:


#TEMP DB in RAM

#Push Pandas df --> temp db

#sql query on temp db


# In[34]:


temp_db = create_engine('sqlite:///:memory:', echo = True)


# In[35]:


data = df.to_sql(name = "Sales", con = temp_db)


# In[36]:


with temp_db.connect() as conn:
    #make connection
    #run code
    result = conn.execute(text("Select * from Sales"))
    #auto close connection
    


# In[37]:


result.all()


# In[38]:


def create_table_definition(df):
    prompt = '''### sqlite SQL table, with it properties: 
    #
    # Sales({})
    #
    '''.format(", ".join(str(col) for col in df.columns))
    
    return prompt


# In[39]:


",".join(str(col) for col in df.columns)


# In[40]:


print(create_table_definition(df))


# In[41]:


def prompt_input():
    nlp_text = input("Enter the info you want: ")
    return nlp_text


# In[42]:


#prompt_input()


# In[43]:


def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_init_string = f'### Provide only SQL code A query to answer: {query_prompt}\nSELECT' 
    return definition + query_init_string


# In[44]:


nlp_text = prompt_input()
combine_prompts(df, nlp_text)


# In[45]:


response = openai.Completion.create(
    model='davinci',
    prompt = combine_prompts(df, nlp_text),
    temperature = 0,
    max_tokens = 150,
    top_p = 1.0, 
    frequency_penalty = 0,
    presence_penalty = 0,
    stop=['#', ';']
)


# In[46]:


#response["choices"][0]["text"]


# In[47]:


def handle_response(response):
    query = response["choices"][0]["text"].split("\n")[0]
    if query.startswith(" "):
        query = "SELECT"+query
    return query


# In[48]:


handle_response(response)


# In[49]:


with temp_db.connect() as conn:
    result = conn.execute(text(handle_response(response)))


# In[50]:


result.all()

