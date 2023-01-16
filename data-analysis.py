#!/usr/bin/env python
# coding: utf-8

# **Importing Libraries**

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# **Read Data**

# In[2]:


power=pd.read_csv('PowerGeneration.csv')
print('Data Shape :', power.shape)


# In[3]:


power.head()


# In[4]:


power.info()


# In[5]:


power.describe()


# # Feature Engineering 

# In[10]:


sns.heatmap(power.isnull(),yticklabels=False,cbar=False)


# In[11]:


from pandas_profiling import ProfileReport


# In[12]:


pp_report=ProfileReport(power)
pp_report


# In[13]:


sns.jointplot(x='Total Cap. Under Maintenace (MW)',y='Planned Maintanence (MW)',data=power)


# In[14]:


power.drop('Dates',inplace=True,axis=1)
power.drop('Power Station',inplace=True,axis=1)
power.head()


# In[15]:


sns.heatmap(power,cmap='magma',linecolor='white')


# In[ ]:




