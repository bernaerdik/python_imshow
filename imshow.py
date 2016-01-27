# python_imshow

# coding: utf-8
import numpy as np
# In[1]:

import numpy as np


# In[2]:

import matplotlib.pyplot as pit


# In[3]:

get_ipython().magic(u'matplotlib inline')


# In[4]:

points=np.arange(-5,5,0.01)



# In[6]:

dx,dy=np.meshgrid(points,points)


# In[8]:

z =(np.sin(dx) + np.sin(dy))


# In[11]:

print pit.imshow(z)
