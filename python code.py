#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[14]:


salary = pd.read_csv(r"C:\Users\huzai\Downloads\ds_salaries.csv")


# In[15]:


salary


# In[17]:


salary.drop('Unnamed: 0', axis=1, inplace=True)


# In[18]:


salary


# In[19]:


salary.isnull().sum()


# In[20]:


salary.info()


# In[21]:


salary.shape


# In[22]:


salary['salary_in_usd'].mean()


# In[23]:


salary['salary_in_usd'].max()


# In[24]:


salary['salary_in_usd'].min()


# In[25]:


salary[salary['salary_in_usd'] == salary['salary_in_usd'].max()]


# In[26]:


salary[salary['salary_in_usd'] == salary['salary_in_usd'].min()]


# In[27]:


salary['work_year'].value_counts()


# In[28]:


sns.countplot(x='work_year',data=salary)


# In[29]:


salary_per_year = salary.groupby('work_year').mean()['salary_in_usd'].reset_index().sort_values(by='salary_in_usd')
salary_per_year


# In[30]:


plt.figure(figsize=(12,6))
plt.title("Average Salary of Data Science Jobs per Year")
sns.barplot(x=salary_per_year['work_year'], y=salary_per_year['salary_in_usd'])
plt.xlabel("Year")
plt.ylabel("Number of Average Salary in USD")


# In[31]:


sns.violinplot(x='work_year',y='salary_in_usd',data=salary,palette='rainbow')


# In[32]:


sns.distplot(salary['salary_in_usd'])


# In[33]:


salary['job_title'].nunique()


# In[34]:


salary['job_title'].unique()


# In[35]:


salary['job_title'].value_counts().head(10)


# In[36]:


salary.groupby('job_title').mean()['salary_in_usd'].reset_index().sort_values(['salary_in_usd'],ascending=False).head(10)


# In[37]:


salary['company_location'].nunique()


# In[38]:


salary['company_location'].value_counts().head(10)


# In[40]:


salary[(salary['company_location']=='US')]['job_title'].value_counts().head()


# In[41]:


salary['employee_residence'].value_counts().head(10)


# In[42]:


salary['experience_level'].value_counts()


# In[43]:


sns.countplot(x='experience_level', data=salary)


# In[44]:


explvl_sal = salary.groupby('experience_level').mean()['salary_in_usd'].reset_index().sort_values(['salary_in_usd'])
explvl_sal


# In[45]:


plt.figure(figsize=(9,6))
plt.title("Average Salary of Data Science Jobs by Experience Level")
sns.barplot(x=explvl_sal['experience_level'], y=explvl_sal['salary_in_usd'])
plt.xlabel("Experience Level")
plt.ylabel("Number of Average Salary in USD")


# In[46]:


salary['employment_type'].value_counts()


# In[47]:


sns.countplot(x='employment_type', data=salary)


# In[48]:


salary['company_size'].value_counts()


# In[49]:


sns.countplot(x='company_size', data=salary)


# In[50]:


mean_sal_com = salary.groupby('company_size').mean()['salary_in_usd'].reset_index()
mean_sal_com


# In[51]:


plt.figure(figsize=(8,6))
plt.title("Average Salary of Data Science Jobs by Company Size")
sns.barplot(x=mean_sal_com['company_size'], y=mean_sal_com['salary_in_usd'])
plt.xlabel("Company Size")
plt.ylabel("Number of Average Salary in USD")


# In[52]:


ds_cntry_sal = salary.groupby('company_location').mean()['salary_in_usd'].reset_index().sort_values(['salary_in_usd'],ascending=False).head(10)
ds_cntry_sal


# In[53]:


plt.figure(figsize=(14,6))
plt.title("High Average Salary of Data Science Jobs by Country")
sns.barplot(x=ds_cntry_sal['company_location'], y=ds_cntry_sal['salary_in_usd'])
plt.xlabel("Country")
plt.ylabel("Number of Average Salary in USD")


# In[54]:


ds_cntry_sal2 = salary.groupby('company_location').mean()['salary_in_usd'].reset_index().sort_values(['salary_in_usd'],ascending=True).head(10)
ds_cntry_sal2


# In[55]:


plt.figure(figsize=(14,6))
plt.title("Least Average Salary of Data Science Jobs by Country")
sns.barplot(x=ds_cntry_sal2['company_location'], y=ds_cntry_sal2['salary_in_usd'])
plt.xlabel("Country")
plt.ylabel("Number of Average Salary in USD")


# In[56]:


salary['remote_ratio'].value_counts()


# In[57]:


sns.countplot(x='remote_ratio', data=salary)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




