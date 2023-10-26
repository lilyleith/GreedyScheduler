#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[28]:


t = int(input())
tcount = 0

schedules = [None] * t
while tcount < t:
    n = int(input())
    ncount = 0
    schedules[tcount] = [None] * n
    
    while ncount < n:
        job = input().replace('\n','')
        job = job.split(' ')
        job[0] = int(job[0])
        job[1] = int(job[1])
        schedules[tcount][ncount] = job
        ncount += 1
    schedules[tcount] = sorted(schedules[tcount], key = lambda item:item[1])
    tcount += 1  


# In[29]:


new_schedules = [None] * t
tcount = 0
while tcount < t:
    new_schedules[tcount] = []
    last_finish = 0
    ncount = 0
    while len(schedules[tcount]) > 0:
        
        job = schedules[tcount][0]
        
       
        if job[0] < last_finish:
            schedules[tcount].remove(job)
          
        else:
            last_finish = job[1]
            new_schedules[tcount].append(job)
            schedules[tcount].remove(job)
            
        ncount += 1
    print(len(new_schedules[tcount]))
    tcount += 1


# In[ ]:




