#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv(r'C:\Users\Admin\Desktop\data.csv')
print(data)


# In[16]:


import matplotlib.pyplot as plt
df=pd.DataFrame(data)
x=df['x']
y=df['y']
print("bargraph \n")
plt.figure(figsize=(3,3))
plt.bar(x,y)
plt.figure(figsize=(3,3))
plt.scatter(x,y)
plt.figure(figsize=(3,3))
plt.plot(x,y)


# In[50]:


import pandas as pd
da = pd.read_csv(r"C:\Users\Admin\Desktop\marks.csv")
print(da)
df=pd.DataFrame(da)
maths=df['Maths'].sum()
science =df['science'].sum()
physics =df['physics'].sum()
english=df['english'].sum()

marks=['maths','science' ,'physics','english']
totals=[maths,science ,physics,english]
plt.pie(totals, labels=marks, autopct='%1.1f%%')
plt.show()


# In[59]:



import kagglehub

df =  kagglehub.dataset_download( "y0ussefkandil/bmw-sales2010-2024")
print(df)


# In[61]:


data=pd.read_csv(r'C:\Users\Admin\.cache\kagglehub\datasets\y0ussefkandil\bmw-sales2010-2024\versions\1\BMW sales data (2010-2024).csv')
print(data.head())


# In[ ]:




