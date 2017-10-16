import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import csv
import matplotlib.pyplot as plt
from pylab import *
df  = pd.read_csv('raycom-people.csv')
df[u'HireDate']= pd.to_datetime(df[u'HireDate'],format='%Y-%m-%d')
df1 = df.set_index('HireDate')
j=1
list = [len(df1[str(2006)]),];

for i in range(2005,2017):
   
    list += [len(df1[str(i)]),]
    j +=1
    i +=1
s1=Series(list)
list2 = [2005,]
df3 = df1[df1.TerminationDate <>'None']
j = 1
list1 = [len(df3[str(i)]),];
for i in range(2005,2017):
    print i+1
    list2 += [(i+1),] 
    list1 += [len(df3[str(i)]),]
    j +=1
    i +=1
del list2[0]
print list2
s2=Series(list1)

plt.plot(s1)
plt.plot(s2)
plt.ylim(0,200)
plt.xlabel('Year')
plt.ylabel('Number of Associates')
plt.title('The change of Associates')

#plt.xticks('2006','2006','2006','2006','2006','2006','2006','2006','2006','2006','2006','2006','2006')
plt.show()

