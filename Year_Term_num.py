#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('raycom-people.csv')
df['HireDate']=pd.to_datetime(df['HireDate'])
df1 = df[df.TerminationDate <>'None']
df1 = df1.set_index('HireDate')
i = 2005
j = 1
list = [len(df1[str(2006)]),];

for i in range(2005,2017):
    print len(df1[str(i)]),
    list += [len(df1[str(i)]),]
    j +=1
    i +=1
    print i
    print list
df = pd.DataFrame(list)
#print df
group_labels = ['a', 'b','c','d','e','f']
plt.plot(df)
plt.show()

