import numpy as np
import pandas as pd

a = np.array([[1,2,3],[4,5,6]])

'''
a = [
    [1,2,3],
    [4,5,6]
    ]
sum() 전체 합계 반환
sum(axis=0) 열별 합계 반환
sum(axis=1) 행별 합계 반환
'''

print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

'''
mean() 전체평균
mean(axis=0) 열별 평균
mean(axis=1) 행별 평균
'''

df = pd.DataFrame({
    'col1':['one','two','three','four','five'],
    'col2':[6,7,8,9,10]
})

print(df)
print(df['col1'].dtype)
print(df['col2'].dtype)

my_df=pd.DataFrame({
    '실수':pd.Series(dtype='float'),
    '정수':pd.Series(dtype='int'),
    '범주형':pd.Series(dtype='category'),
    '논리':pd.Series(dtype='bool'),
    '문자열':pd.Series(dtype='str')
})
print(my_df)
print(my_df.dtypes)

my_df = pd.DataFrame({
    'name':['issac','bomi'],
    'birthmonth':[5,4]
})

url = "https://raw.githubusercontent.com/YoungjinBD/data/main/examscore.csv"
mydata = pd.read_csv(url)

print(mydata.head())
print(mydata.shape)

'''
   student_id gender  midterm  final
0           1      F       38     46
1           2      M       42     67
2           3      F       53     56
3           4      M       48     54
4           5      M       46     39

행과 열의 갯수(30, 4)
행 : 30 , 열 4
'''

print(my_df['name'])

print(my_df.iloc[:,0])
print(my_df.shape)

print(mydata[mydata['midterm']<=15])

print(mydata.loc[mydata['midterm']<=15])

print(mydata.loc[mydata['midterm']<=15,['student_id', 'final']])


print('---------------------------------------------------')

print(mydata[mydata['midterm'].isin([28,38,52])].head)

print(mydata.loc[~mydata['midterm'].isin([28,38,52]),['student_id','final']].head)