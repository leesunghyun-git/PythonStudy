import pandas as pd
import numpy as np

mydata = pd.DataFrame({
    'student_id':[1,2,3,4,5],
    'gender':['F','M','F','M','M'],
    'miderm':[38,42,53,48,36],
    'final':[46,67,56,54,39]
})

mydata.iloc[0,1]=np.nan
mydata.iloc[4,0]=np.nan
print(mydata.head())
print(mydata.shape)

print("gender 열의 빈칸 갯수 :",mydata['gender'].isna().sum())
print("stduent_id 열의 빈칸 갯수 :",mydata['student_id'].isna().sum())

complet_row =mydata.dropna()
print("완전한 행의 수 : ",len(complet_row))
print(complet_row)

mydata['total']=mydata['miderm']+mydata['final']
print(mydata.iloc[0:3,[3,4]])
print(mydata.shape)
print(mydata)

mydata=pd.concat([mydata,(mydata['total']/2).rename('average')],axis=1)
print(mydata.head())

mydata.rename(columns={'average':'my_average'},inplace=True)
print(mydata.head())

del mydata['gender']
print(mydata.head())