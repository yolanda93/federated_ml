#!/usr/bin/env python
# coding: utf-8

# In[1]:


import syft as sy
from syft.grid.public_grid import PublicGridNetwork

import torch as th

import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

import torchvision
from torchvision import datasets, transforms


# In[4]:


grid_address = "http://0.0.0.0:7000"  # address
hook = sy.TorchHook(th)

my_grid = PublicGridNetwork(hook, grid_address)


# In[5]:


data = my_grid.search("#X", "#mnist", "#dataset")  # images
target = my_grid.search("#Y", "#mnist", "#dataset")  # labels

data = list(data.values())  # returns a pointer
target = list(target.values())  # returns a pointer


# In[6]:


print(data)
print(target)


# In[ ]:




