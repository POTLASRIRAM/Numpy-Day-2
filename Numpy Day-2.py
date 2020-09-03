
# ### Numpy copy vs view

# In[23]:


#copy
import numpy as np
a=np.array([1,2,3,4,5])
b=a.copy()
a[0]=20
print(a)
print(b)


# In[24]:


#view
a=np.array([1,2,3,4])
b=a.view()
a[0]=20
print(a)
print(b)


# In[25]:


#Cjeck if array own's data or not
# by using base attribute
a=np.array([1,2,3,4,5])
b=a.copy()
c=a.view()
print(b.base)
print(c.base)


# ### Numpy array shape

# In[27]:


# Getiing the shape of array
a=np.array([[1,2,3,4],[1,2,3,4]])
print(a.shape)


# ### Numpy array reshaping

# In[11]:


#Reshape from 1-D t0 2-D
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(6,2)
b


# In[12]:


# Reshape from 1-D to 3-D
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape(2,3,2)
b


# In[13]:


# Reshaping from 3-D to 2-D
a=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
b=a.reshape(4,4)
b


# In[14]:


# Flattening the array's
#from 2-D to 1-D
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(-1)
b


# In[15]:


#From 3-D to 1-D
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
b=a.reshape(-1)
b


# ### Numpy array iteration

# In[16]:


# iterating 1-D array
a=np.array([1,2,3])
for x in a:
    print(x)


# In[17]:


#iterating 2-D array
a=np.array([[1,2,3,4],[5,6,7,8]])
for x in a:
    for y in x:
        print(y)


# In[18]:


#iterating 3-D array
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
for x in a:
    for y in x:
        for z in y:
            print(z)


# In[19]:


# Iterating array using nditer()
a=np.array([[1,2],[3,4]])
for x in np.nditer(a):
    print(x)


# In[20]:


# Iterating with different step size
a=np.array([1,2,3,4,5,6])
for x in np.nditer(a[::2]):
    print(x)


# In[21]:


# Enumerated iteration using ndenumerate()
a=np.array([1,2,3,4,5])
for i,x in np.ndenumerate(a):
    print(i,x)


# ### Numpy joining array

# In[22]:


# Joining numpy array
#concatenate()
# 1-D
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
c=np.concatenate((a,b))
c


# In[23]:


# 2-D
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[1,2,3,4],[5,6,7,8]])
c=np.concatenate((a,b))
c


# In[24]:


# Joining array's using stack function's
# vstack,hstack
# 1-D hstack
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4])
c=np.hstack((a,b))
c


# In[26]:


#2-D hstack
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
c=np.hstack((a,b))
c


# In[27]:


# 1-D vstack
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=np.vstack((a,b))
c


# In[28]:


# 2-D vstack
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[1,2,3,4],[6,7,87,8]])
c=np.vstack((a,b))
c


# ### Numpy splitting array

# In[32]:


# Splitting numpy array
# using array_split()
a=np.array([1,2,3,4,5,6])
b=np.array_split(a,3)
print(b[0])
print(b[1])
print(b[2])


# In[46]:


# Splitting 2-D
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array_split(a,3)
print(b)


# In[38]:


# Splitting along columns(2-D)
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b=np.array_split(a,2,axis=1)
b


# ### Numpy searching array's

# In[47]:


# array search using where()
a=np.array([1,2,3,4,5,6,7,8])
b=np.where(a==4)
b


# In[48]:


# Searching and printing even indexes and odd index values
# even
b=np.where(a%2==0)
b


# In[49]:


# odd
b=np.where(a%2==1)
b


# In[51]:


# Search sorted
#searchsorted()
b=np.searchsorted(a,9)
b


# In[52]:


# for multiple values
b=np.searchsorted(a,[10,11,12])
b


# In[ ]:




