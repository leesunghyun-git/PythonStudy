import pandas as pd

data = {
    'date':['2024-01-01 12:34:56','2024-02-01 23:45:01','2024-03-01 06:07:08','2021-04-01 14:15:16'],
    'value':[100,201,302,404]
}
df = pd.DataFrame(data)

print(df)

df['date']=pd.to_datetime(df['date'])
print(df.info())
'''
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   date    4 non-null      datetime64[ns]
 1   value   4 non-null      int64
'''
print('-----------------------------------')
print(pd.to_datetime('02-2024-01',format='%m-%Y-%d'))

'''
2024-02-01 00:00:00
'''
print('-----------------------------------')
print(pd.to_datetime('2024년 01월 01일',format='%Y년 %m월 %d일'))
'''
2024-01-01 00:00:00
'''
# 년 추출
df['year']=df['date'].dt.year
#월 추출
df['month']=df['date'].dt.month

#일 추출
df['day']=df['date'].dt.day

#요일 추출

df['wday']=df['date'].dt.day_name()
df['wday2']=df['date'].dt.weekday

#시간 추출
df['hour']=df['date'].dt.hour

#분 추출

df['minute']=df['date'].dt.minute

#초 추출

df['second'] =df['date'].dt.second

#년-월-일
print('--------------------------')
print(df['date'].dt.date)

print(df.head(2))

'''
0    2024-01-01
1    2024-02-01
2    2024-03-01
3    2021-04-01
Name: date, dtype: object
                 date  value  year  month  day      wday  wday2  hour  minute  second
0 2024-01-01 12:34:56    100  2024      1    1    Monday      0    12      34      56
1 2024-02-01 23:45:01    201  2024      2    1  Thursday      3    23      45       1

'''

current_date = pd.to_datetime('2024-05-01')

df['days_diff']=(current_date-df['date']).dt.days

print(df.head(2))

'''
                 date  value  year  month  day      wday  wday2  hour  minute  second  days_diff
0 2024-01-01 12:34:56    100  2024      1    1    Monday      0    12      34      56        120
1 2024-02-01 23:45:01    201  2024      2    1  Thursday      3    23      45       1         89
'''

print('----------------------------')

date_range=pd.date_range(start='2021-01-01',end='2021-01-10',freq='D')
print(date_range)
'''
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08',
               '2021-01-09', '2021-01-10'],
              dtype='datetime64[ns]', freq='D')
'''

df['date2']  = pd.to_datetime(dict(year=df.year,month=df.month,day=df.day))

print(df[['date','date2']])