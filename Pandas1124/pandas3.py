import pandas as pd

data = {
    'date':['2024-01-01 12:34:56','2024-02-01 23:45:01','2024-03-01 06:07:08','2021-04-01 14:15:16'],
    'value':[100,201,302,404]
}
df=pd.DataFrame(data)

print(df)
print(df.info())
'''
                  date  value
0   2024-010- 12:34:56    100
1  2024-02-01 23:45:01    201
2  2024-03-01 06:07:08    302
3  2021-04-01 14:15:16    404
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   date    4 non-null      object
 1   value   4 non-null      int64
dtypes: int64(1), object(1)
'''

df['date']=pd.to_datetime(df['date'])
print(df.head(4))
'''
None
                 date  value
0 2024-01-01 12:34:56    100
1 2024-02-01 23:45:01    201
2 2024-03-01 06:07:08    302
3 2021-04-01 14:15:16    404
'''
print(df.info())
'''
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   date    4 non-null      datetime64[ns]
 1   value   4 non-null      int64
'''

'''


'''

  