
# ### Numpy array sort

# In[1]:


# Sorting array's using sort()
#numerical's
import numpy as np
a=np.array([1,0,3,2])
print(np.sort(a))


# In[2]:


# character's
a=np.array(['banana','apple','cherry'])
print(np.sort(a))


# In[3]:


#Boolean
a=np.array([True,False,False])
print(np.sort(a))


# In[4]:


#Sorting 2-D array
a=np.array([[3,1,5],[5,8,6]])
print(np.sort(a))


# ### Numpy array filter

# In[45]:


# Getting element's out of an existing array and creating new array out of them 
a=np.array([20,23,24,21,45])
x=[True,False,True,True,True]
b=a[x]
b


# In[6]:


# Creating array filter by using iteration
f_a = []
for x in a:
    if x>25:
        f_a.append(True)
    else:
        f_a.append(False)
b=a[f_a]
b


# In[7]:


f_a=a>22
b=a[f_a]
print(f_a)
print(b)


# In[8]:


a=np.array([[20,21,22,2,3,24],[1,2,3,4,56,6]])
f_a = (a%2==0)
b=a[f_a]
b


# ### Random Number's in Numpy

# In[9]:


#Generating random number's using random module from numpy
#Random integer's genertion
from numpy import random
x=random.randint(100)
x


# In[10]:


#1-D
x=random.randint(100,size=(7))
x


# In[12]:


# 2-D
x=random.randint(100,size=(3,4))
x


# In[15]:


# 3-D
x=random.randint(100,size=(2,1,3))
x


# In[3]:


# Generating random float's using rand()
from numpy import random
x=random.rand(70)
x


# In[20]:


# Generating Random Number from Array using choice() method
a=random.choice([3,1,5,6,8])
print(a)


# In[21]:


a=random.choice([1,23,6,4,5],size=(3,5))
a


# In[ ]:




