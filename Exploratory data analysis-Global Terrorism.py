#!/usr/bin/env python
# coding: utf-8

# # LGM Data Science Internship | August 2021 
# 
# Task: Exploratory Data Analusis-Terrorism
# 
# Level: Intermidiate
# 
# Author: Rashi Gupta
# 
# ->Perform 'Exploratory Data Analysis' on dataset Global Terrorism'.
# 
# ->As a security/defense analyst, try to find out the zone of terrorism.
# 
# ->What all security issues and insights you can derive by EDA?
# 
# ### Dataset Used: Global Terorrism
# ### Dataset available at: [Click here](https://drive.google.com/file/d/1luTU7xBvI7QAGPbQMxEHcgKUi9d6UeP_/view)

# # Importing required libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data_frame = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='latin1')
data_frame.head()


# In[3]:


data_frame.tail()


# In[4]:


data_frame.info()


# In[5]:


data_frame.describe()


# # Printing all the columns

# In[6]:


data_frame.columns.values


# # Printing Column wise info for the data frame to take further decisions 

# In[7]:


data_frame.info(verbose=True, null_counts=True)


# # Considering Columns based on above info (eliminating some since most of their values are null) and renaming as per convenience

# In[8]:


data_frame.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City',
                           'latitude':'latitude','longitude':'longitude','summary':'summary','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype',
                           'weaptype1_txt':'Weapon','nkill':'kill','nwound':'Wound'},inplace=True) 
#inplace allows us to save the value there i.e. updates the dataframe with required modification


# In[9]:


data_frame = data_frame[['Year','Month','day','Country','State','Region','City','latitude','longitude',"Attacktype",'kill','Wound','target1','summary',
                         'Group','Targettype','Weapon','motive']]


# In[10]:


data_frame.head()


# In[11]:


data_frame.shape
#To get number of rows and columns


# # Preprocessing the data

# In[12]:


data_frame.isna().sum()


# In[13]:


data_frame['Wound'] = data_frame['Wound'].fillna(0)
data_frame['kill'] = data_frame['kill'].fillna(0)


# In[14]:


data_frame['Casualities'] = data_frame['kill'] + data_frame['Wound']


# In[15]:


data_frame.info()


# # Finding numeric columns for visualization

# In[16]:


data_frame.select_dtypes('number')


# # Visualization

# In[17]:


year = data_frame['Year'].unique()
years_count = data_frame['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (20,10))
sns.barplot(y = year,
           x = years_count,
           palette = "bright",
           orient="h")
plt.xticks(rotation = 0)
plt.xlabel('Number of Attacks',fontsize=20)
plt.ylabel('Year of Attack',fontsize=20)
plt.title('Number of Attacks in the years',fontsize=25)
plt.show()


# In[18]:


pd.crosstab(data_frame.Year, data_frame.Region).plot(kind='area',stacked=False,figsize=(20,10))
plt.title('Terrorist Activities By Region In Each Year',fontsize=25)
plt.ylabel('Number of Attacks',fontsize=20)
plt.xlabel("Year",fontsize=20)
plt.show()


# In[19]:


attack = data_frame.Country.value_counts()[:20]
attack
#to obtain 20 countries affected


# In[20]:


data_frame.Group.value_counts()[1:20]
#to obtain top 20 attacking groups


# In[30]:


plt.subplots(figsize=(20,10))
sns.barplot(data_frame['Country'].value_counts()[:20].index,data_frame['Country'].value_counts()[:20].values,palette="icefire")
plt.title('Top 20  Affected Countries',fontsize=25)
plt.xlabel('Country',fontsize=20)
plt.ylabel('Count',fontsize=20)
plt.xticks(rotation = 90)
plt.show()


# In[22]:


df = data_frame[['Year','kill']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4,color='red')
plt.xticks(rotation = 90)
plt.title("Death due to Attack",fontsize=25)
plt.ylabel("Number of people killed",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)


# In[25]:


data_frame['City'].value_counts().to_frame().sort_values('City',axis=0,ascending=False).head(20).plot(kind='bar',figsize=(20,10),color='green')
plt.xticks(rotation = 90)
plt.xlabel("City",fontsize=20)
plt.ylabel("Number of attack",fontsize=20)
plt.title("Top 20 most effected city",fontsize=25)
plt.show()


# In[26]:


data_frame['Attacktype'].value_counts().plot(kind='bar',figsize=(20,10),color='brown')
plt.xticks(rotation = 90)
plt.xlabel("Type of Attack",fontsize=20)
plt.ylabel("Attack Count",fontsize=25)
plt.title("Attack types with Attack count",fontsize=25)
plt.show()


# In[27]:


data_frame[['Attacktype','kill']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['darkslateblue'])
plt.xticks(rotation=90)
plt.title("Number of people killed due to attacks ",fontsize=25)
plt.ylabel('Number of people killed',fontsize=20)
plt.xlabel('Type of Attack',fontsize=20)
plt.show()


# In[28]:


data_frame[['Attacktype','Wound']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color=['orange'])
plt.xticks(rotation=90)
plt.title("Number of people wounded due to attack",fontsize=25)
plt.ylabel('Number of people wounded',fontsize=20)
plt.xlabel('Type of Attack',fontsize=20)
plt.show()


# In[29]:


plt.subplots(figsize=(20,10))
sns.countplot(data_frame["Targettype"],order=data_frame['Targettype'].value_counts().index,palette="icefire");
plt.xticks(rotation=90)
plt.xlabel("Target",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.title("Number of Attacks on different targets",fontsize=20)
plt.show()


# In[31]:


data_frame['Group'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='#c7080b',figsize=(20,10))
plt.title("Top 10 Terrorist Group",fontsize=25)
plt.xlabel("terrorist group name",fontsize=20)
plt.ylabel("Attack Count",fontsize=20)
plt.show()


# In[32]:


data_frame[['Group','kill']].groupby(['Group'],axis=0).sum().drop('Unknown').sort_values('kill',ascending=False).head(10).plot(kind='bar',color='#78292a',figsize=(20,10))
plt.title("Top 10 terrorist group (ranked by people killed)",fontsize=20)
plt.xlabel("Terrorist Group",fontsize=15)
plt.ylabel("No of people killed",fontsize=15)
plt.show()


# # Conclusion and Results :

# ->Country with the most attacks: Iraq
# 
# ->City with the most attacks: Baghdad
# 
# ->Region with the most attacks: Middle East & North Africa
# 
# ->Year with the most attacks: 2014
# 
# ->Month with the most attacks: 5
# 
# ->Group with the most attacks: Taliban
# 
# ->Most Attack Types: Bombing/Explosion

# In[ ]:




