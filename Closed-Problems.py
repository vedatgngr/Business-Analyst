#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pm4py
#Burada kodumuzun içine kullandığımız kütüphaneleri içeri aktardık.
log = pm4py.read_xes(os.path.join("tests","input_data","C:/Users/vedat/vedatdata/BPI_Challenge_2013_closed_problems.xes"))
#programda kullanacağımız verinin yolunu pm4py kütüphanesiyle okuyup log değişkeninin içerisine aktardık.
dfg, start_activities, end_activities = pm4py.discover_dfg_typed(log)
#yukarıdan gelen değişkenin başlangıç ve bitiş noktalarının pm4py kütüphanesinden gelen akış şemasına ekledik.
pm4py.view_dfg(dfg, start_activities, end_activities)
#bu akış şemasının görsel çıktısı için pm4py kütüphanesinin viev_dfg uzantısını kullandık.


# In[ ]:




