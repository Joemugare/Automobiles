#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df =pd.read_csv('Automobile.csv')


# # Count the number of cars from each origin

# In[5]:


origin_counts = df['origin'].value_counts()


# # Create a pie chart to visualize the distribution of car origins

# In[6]:


plt.figure(figsize=(8, 6))
plt.pie(origin_counts, labels=origin_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Car Origins')
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is drawn as a circle.
plt.show()


# In[ ]:




