import csv 
import plotly.express as px 
import pandas as pd 
import math
with open('project.csv') as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata[0]
totalmarks=0
totalentries=len(data)
for i in data:
    totalmarks+=int(i)
mean=totalmarks/totalentries
print(mean)
sqlist=[]
for i in data:
    a=int(i)-mean
    a=a**2
    sqlist.append(a)
sum=0
for i in sqlist:
    sum=sum+i
result=sum/(len(data)-1)
standarddevation=math.sqrt(result)
print(standarddevation)