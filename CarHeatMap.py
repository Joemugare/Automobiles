#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


df =pd.read_csv('Automobile.csv')


# # Extract car names and drop the 'name' column from the DataFrame

# In[12]:


car_names = df['name']
df = df.drop(columns=['name'])


# # Concatenate car names with the original DataFrame

# In[28]:


car_data = pd.concat([car_names, df], axis=1)


# # Display car names along with details

# In[30]:


print("Car Details:")
print(car_data.to_string(index=False))


# # Compute the correlation matrix

# In[21]:


correlation_matrix = df.corr()


# # Create a heatmap using Seaborn

# In[17]:


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, xticklabels=df.columns, yticklabels=df.columns)
plt.title('Correlation Heatmap')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.yticks(rotation=0)   # Keep y-axis labels horizontal
plt.show()


# In[ ]:




