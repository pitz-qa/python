#!/usr/bin/env python
# coding: utf-8

# # How to open file

# In[24]:


with open('/home/piyush/Downloads/piyush.txt') as players_data:
    players_data.read()


# # How to use tab delimited in file

# In[28]:


with open('/home/piyush/Downloads/piyush.txt', 'a') as players_data:
    players_data.write('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format('Trey', 'Burke', '23', '1.85', '2013', '79.4', '23.2'))

