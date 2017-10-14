import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import csv
import matplotlib.pyplot as plt
from pylab import *
df  = pd.read_csv('raycom-people.csv')
df[u'HireDate']= pd.to_datetime(df[u'HireDate'],format='%Y-%m-%d')

df1 = df.set_index('HireDate')
df_t= df1
#print df_t
#list_t=[len(df_t[str(2006)]),len(df_t[str(2006):str(2007)])--len(df3['2006':'2007']),len(df_t[str(2006):str(2008)])-len(df3['2006':'2008']),len(df_t[str(2006):str(2009)])-len(df3['2006':'2009']),len(df_t[str(2006):str(2010)])-len(df3['2006':'2010']),len(df_t[str(2006):str(2011)])-len(df3['2006':'2011']),len(df_t[str(2006):str(2012)])-len(df3['2006':'2012']),len(df_t[str(2006):str(2013)])-len(df3['2006':'2013']),len(df_t[str(2006):str(2014)])-len(df3['2006':'2014']),len(df_t[str(2006):str(2015)])-len(df3['2006':'2015']),len(df_t[str(2006):str(2016)])-len(df3['2006':'2016']),len(df_t[str(2006):str(2017)])-len(df3['2006':'2017'])]
#print list_t
j=1
list = [len(df1[str(2006)]),];

for i in range(2005,2017):
   
    list += [len(df1[str(i)]),]
    j +=1
    i +=1
del list[0]
print list
s1=Series(list)

list2 = [2005,]
df3 = df1[df1.TerminationDate <>'None']
j = 1
print "--------i--------"
print i
list1 = [len(df3[str(2006)]),];
for i in range(2005,2017):
   
    list2 += [(i+1),] 
    list1 += [len(df3[str(i)]),]
    j +=1
    i +=1
del list2[0]
del list1[0]
print list2
print list1
s2=Series(list1)

list_t=[len(df_t[str(2006)]),len(df_t[str(2006):str(2007)])--len(df3['2006':'2007']),len(df_t[str(2006):str(2008)])-len(df3['2006':'2008']),len(df_t[str(2006):str(2009)])-len(df3['2006':'2009']),len(df_t[str(2006):str(2010)])-len(df3['2006':'2010']),len(df_t[str(2006):str(2011)])-len(df3['2006':'2011']),len(df_t[str(2006):str(2012)])-len(df3['2006':'2012']),len(df_t[str(2006):str(2013)])-len(df3['2006':'2013']),len(df_t[str(2006):str(2014)])-len(df3['2006':'2014']),len(df_t[str(2006):str(2015)])-len(df3['2006':'2015']),len(df_t[str(2006):str(2016)])-len(df3['2006':'2016']),len(df_t[str(2006):str(2017)])-len(df3['2006':'2017'])]

s3=Series(list_t)

plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],s1,label="New Hires")
plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],s2,label="Leavers")
plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],s3,label="Associates")
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')  
plt.ylim(0,700)

plt.xlabel('Year')
plt.ylabel('Number of Associates')

plt.title('The change of Associates')
plt.annotate('local max', xy=(9,125), xytext=(5, 125),arrowprops=dict(facecolor='red', shrink=0.01),)  
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017'])
plt.legend()
plt.show()

