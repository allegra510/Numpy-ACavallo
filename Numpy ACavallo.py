#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
import numpy as np
print(np.__version__)


# In[2]:


#2
arr_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr_1d)


# In[3]:


#3 
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype = None)
print(iris)


# In[4]:


#4 sepal length, sepal width, petal length, petal width, species name  
petal_width = iris ['f3']
wider_indexes = np.where(petal_width > 1.0)[0]
first_index = wider_indexes[0]
print(first_index)


# In[5]:


#5 
np.random.seed(100)
a = np.random.uniform(1,50, 20)
a[a>30] = 30
a[a<10] = 10
print(a)


# In[ ]:




