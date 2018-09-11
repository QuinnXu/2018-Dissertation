
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# In[31]:


# import data
df1 = pd.read_csv('nottingham-pricing.csv')
df2 = pd.read_csv('nottingham-score.csv')
df3 = pd.read_csv('london-pricing.csv')
df4 = pd.read_csv('london-score.csv')


# # nottingham price

# In[ ]:


# histogram
df1.plot(y = 'price', kind = 'hist', bins = 40, color = 'grey') # use 'bins' to adjust the width of each histgram； # use 'color' to change color
plt.xlabel('price in Nottingham') #label x axis
plt.ylabel('Count') #label y axis
plt.title('Histgram') # name the plot
# plt.xticks([1000,2000,3000,4000,5000],['20%','40%','60%','80%','100%'])
plt.show()


# In[ ]:


# Approximation og Probability distribution function
df1.plot(y = 'price', kind = 'hist', bins = 40, normed = True) 
plt.show()


# In[ ]:


# Cumulative distribution function
df1.plot(y = 'price', kind = 'hist', bins = 20, normed = True, cumulative = True)
plt.show()


# # nottingham score

# In[40]:


df2_score = df2[['Crime Score',
                'Education, Skills and Training Score',
                'Health Deprivation and Disability Score', 
                'Income Score',
                'Living Environment Score']]


# In[ ]:


# pdf
for score in df2_score:
    df2_score.plot(y = score, kind = 'hist', bins = 20, normed = True)
    plt.show()


# In[ ]:


# cdf
for score in df2_score: 
    df2_score.plot(y = score, kind = 'hist', bins = 20, normed = True, cumulative = True)
    plt.show()


# # london price

# In[ ]:


# pdf
df3.plot(y='price',kind = 'hist',bins = 100, normed = True)
plt.show()


# In[ ]:


# cdf
df3.plot(y='price',kind = 'hist',bins = 100, normed = True, cumulative = True)
plt.show()


# # london score

# In[ ]:


# pdf
df4.plot(y='IMD Score',kind = 'hist',bins = 20, normed = True)
plt.show()


# In[ ]:


# cdf
df4.plot(y='IMD Score',kind = 'hist',bins = 20, normed = True, cumulative = True)
plt.show()

