#!/usr/bin/env python
# coding: utf-8

# # How to Read a CSV File

# In[21]:


#import necessary modules
import csv
with open('/home/piyush/Downloads/data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)


# # How to Read a CSV as a Dictionary

# In[20]:


#import necessary modules
import csv

reader = csv.DictReader(open("/home/piyush/Downloads/data.csv"))
for raw in reader:
    print(raw)


# # How to write CSV File

# In[19]:


#import necessary modules
import csv

with open('/home/piyush/Downloads/data.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])


# # END_CSV
