#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


# In[2]:


df =pd.read_csv('Automobile.csv')


# # Calculate average mpg for different origins

# In[5]:


avg_mpg_by_origin = df.groupby('origin')['mpg'].mean().reset_index()


# # Calculate average mpg for different cylinders

# In[6]:


avg_mpg_by_cylinders = df.groupby('cylinders')['mpg'].mean().reset_index()


# # Create a bar plot to compare average mpg for different origins

# In[22]:


plt.figure(figsize=(8, 6))
sns.barplot(x='origin', y='mpg', data=df, ci=None)
plt.xlabel('Origin')
plt.ylabel('Average MPG')
plt.title('Average MPG for Different Origins')
plt.savefig('average_mpg_by_origin.png')  # Save the bar plot as an image file
plt.show()


# In[17]:





# # Create a bar plot to compare average mpg for different cylinders

# In[21]:


plt.figure(figsize=(8, 6))
sns.barplot(x='cylinders', y='mpg', data=df, ci=None)
plt.xlabel('Cylinders')
plt.ylabel('Average MPG')
plt.title('Average MPG for Different Cylinders')
plt.savefig('average_mpg_by_cylinders.png')  # Save the bar plot as an image file
plt.show()


# # Export the data to a new CSV file

# In[26]:


avg_mpg_by_origin.to_csv('C:/Users/Qunta/Downloads/average_mpg_by_origin.csv', index=False)
avg_mpg_by_cylinders.to_csv('C:/Users/Qunta/Downloads/average_mpg_by_cylinders.csv', index=False)


# # Get the current working directory and display it

# In[27]:


current_directory = os.getcwd()
print("CSV files saved in:", current_directory)


# # Specify the file names of the image files

# In[29]:


image_file_1 = 'average_mpg_by_origin.png'
image_file_2 = 'average_mpg_by_cylinders.png'

# Construct the full file paths for the image files
image_path_1 = os.path.join(current_directory, image_file_1)
image_path_2 = os.path.join(current_directory, image_file_2)

# Open the image files using the default image viewer or associated application
os.startfile(image_path_1)  # Opens "average_mpg_by_origin.png" with the default image viewer
os.startfile(image_path_2)  # Opens "average_mpg_by_cylinders.png" with the default image viewer


# In[ ]:




