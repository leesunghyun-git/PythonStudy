import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_data.csv')

print(df.info())

print('----------')

print(df.shape)

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 435 entries, 0 to 434
Data columns (total 12 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   datetime    435 non-null    object 
 1   season      435 non-null    int64  
 2   holiday     435 non-null    int64  
 3   workingday  435 non-null    int64  
 4   weather     435 non-null    int64  
 5   temp        435 non-null    float64
 6   atemp       435 non-null    float64
 7   humidity    435 non-null    int64  
 8   windspeed   435 non-null    float64
 9   casual      435 non-null    int64  
 10  registered  435 non-null    int64  
 11  count       435 non-null    int64  
dtypes: float64(3), int64(8), object(1)
memory usage: 40.9+ KB
None
----------
(435, 12)
'''
'''
#1
#계절(season)==1 일때, 가장 대여량이 많은 시간대(hour)를 구하시오
df['datetime']=pd.to_datetime(df['datetime'])
df['hour']=df['datetime'].dt.hour
grouped_df=df.groupby(['season','hour']).agg({'count':'sum'}).reset_index()
max_count_hour=df.loc[df['count'].idxmax(),'hour']

loc[] 라벨 기반 인덱싱
iloc[] 정수 기반 인덱싱
my_df.iloc[:,0]
mydata.loc[mydata['midterm']<=15]

max_count=df['count'].max()
print(max_count)
print(max_count_hour)

max_idx=grouped_df.loc[grouped_df['season']==1]['count'].idxmax()
print(grouped_df.iloc[max_idx])
'''


df['datetime']=pd.to_datetime(df['datetime'])
df['hour']=df['datetime'].dt.hour
#기본세팅
#---------------------------------------------------------------------------------------
#1
season_group_df=df.groupby(['season','hour']).agg({'count':'sum'}).reset_index()
# 시즌별 , 시간별로 그룹화 / count는 통합
print(season_group_df)
season1_df=season_group_df[season_group_df['season']==1]
print(season1_df.head())

max_idx=season1_df['count'].idxmax()
print(season1_df.iloc[max_idx])

#---------------------------------------------------------------------------------

df_sub=df.loc[df.season==1]

summary_data=df_sub.groupby(['season','hour']).agg({'count':'sum'}).reset_index()
print(summary_data)
max_count_hour=summary_data.loc[summary_data['count'].idxmax(),'hour']

max_count=summary_data['count'].max()

print(f'count가 가장 큰 hour은 {max_count_hour}시이며 , 대여량은 {max_count} 입니다')

#2

summary_df=df.groupby('season')['count'].mean().reset_index()
print(summary_df)
'''
   season       count
0       1  103.169811
1       2  218.803922
2       3  265.500000
3       4  218.581197
'''

df['month']=df['datetime'].dt.month
print(df[['count']][df['month']==1].sum())
#count    2567

#4
df['day']=df['datetime'].dt.day
df['date']=df['datetime'].dt.date
print('----------------------------')
date_grouped_df=df.groupby(['date'])['count'].sum().reset_index()
print(date_grouped_df.iloc[date_grouped_df['count'].idxmax()])
'''
date     2012-05-11
count          1398
'''

#5
hour_grouped_df=df.groupby(['hour'])['count'].mean().reset_index()
print(hour_grouped_df)
'''
    hour       count
0      0   43.500000
1      1   52.714286
2      2   32.842105
3      3   12.000000
4      4    6.687500
5      5   17.750000
6      6   58.705882
7      7  208.937500
8      8  483.055556
9      9  260.117647
10    10  144.130435
11    11  182.000000
12    12  277.533333
13    13  290.600000
14    14  266.842105
15    15  255.666667
16    16  373.052632
17    17  519.200000
18    18  447.769231
19    19  322.103448
20    20  210.083333
21    21  196.619048
22    22  113.560000
23    23   77.352941
'''

#6
df['weekday']=df['datetime'].dt.weekday
print(df[['count']][df['weekday']==1].sum())
'''
count    11198
'''

#7

melt_df= df.melt(id_vars=['datetime','season'],value_vars=['casual','registered'],var_name='user_table',value_name='rental_count')
print(melt_df)

melt_grouped_df=melt_df.groupby(['season','user_table']).agg({'rental_count':'mean'}).reset_index()

print(melt_grouped_df)

'''
   season  user_table  rental_count
0       1      casual     14.122642
1       1  registered     89.047170
2       2      casual     48.990196
3       2  registered    169.813725
4       3      casual     55.127273
5       3  registered    210.372727
6       4      casual     29.709402
7       4  registered    188.871795
'''

df2=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/logdata.csv')

print('-----------df2 info---------')
print(df2.info())

print('---------- df2 shape -------------')
print(df2.shape)

print('--------- df2 describe -------')
print(df2.describe)

'''
-----------df2 info---------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 1 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   로그      30 non-null     object
dtypes: object(1)
memory usage: 372.0+ bytes
None
---------- df2 shape -------------
(30, 1)
--------- df2 describe -------
<bound method NDFrame.describe of                                                    로그
0   2024-07-18 12:34:56 User: 홍길동 Action: Login ID...
1   2024-07-18 12:35:00 User: 김철수 Action: Purchase...
2   2024-07-18 12:36:10 User: 이영희 Action: Logout T...
3   2024-07-18 12:37:22 User: 박지성 Action: Login ID...
4   2024-07-18 12:38:44 User: 최강타 Action: Purchase...
5   2024-07-18 12:39:50 User: 장보고 Action: Logout T...
6   2024-07-18 12:40:56 User: 홍길동 Action: Purchase...
7   2024-07-18 12:41:00 User: 김철수 Action: Login ID...
8   2024-07-18 12:42:10 User: 이영희 Action: Purchase...
9   2024-07-18 12:43:22 User: 박지성 Action: Logout T...
10  2024-07-18 12:44:44 User: 최강타 Action: Login ID...
11  2024-07-18 12:45:50 User: 장보고 Action: Purchase...
12  2024-07-18 12:46:56 User: 홍길동 Action: Logout T...
13  2024-07-18 12:47:00 User: 김철수 Action: Purchase...
14  2024-07-18 12:48:10 User: 이영희 Action: Login ID...
15  2024-07-18 12:49:22 User: 박지성 Action: Purchase...
16  2024-07-18 12:50:44 User: 최강타 Action: Logout T...
17  2024-07-18 12:51:50 User: 장보고 Action: Login ID...
18  2024-07-18 12:52:56 User: 홍길동 Action: Purchase...
19  2024-07-18 12:53:00 User: 김철수 Action: Logout T...
20  2024-07-18 12:54:10 User: 이영희 Action: Purchase...
21  2024-07-18 12:55:22 User: 박지성 Action: Login ID...
22  2024-07-18 12:56:44 User: 최강타 Action: Purchase...
23  2024-07-18 12:57:50 User: 장보고 Action: Logout T...
24  2024-07-18 12:58:56 User: 홍길동 Action: Login ID...
25  2024-07-18 12:59:00 User: 김철수 Action: Purchase...
26  2024-07-18 13:00:10 User: 이영희 Action: Logout T...
27  2024-07-18 13:01:22 User: 박지성 Action: Purchase...
28  2024-07-18 13:02:44 User: 최강타 Action: Login ID...
29  2024-07-18 13:03:50 User: 장보고 Action: Purchase...>
'''
df2['날짜정보']=df2['로그'].str.extract(r'([0-9]{4}-[0-9]{2}-[0-9]{2})')
df2['날짜정보']=pd.to_datetime(df2['날짜정보'])
df2['year']=df2['날짜정보'].dt.year
print(df2)
'''
                                                   로그       날짜정보  year
0   2024-07-18 12:34:56 User: 홍길동 Action: Login ID... 2024-07-18  2024
1   2024-07-18 12:35:00 User: 김철수 Action: Purchase... 2024-07-18  2024
2   2024-07-18 12:36:10 User: 이영희 Action: Logout T... 2024-07-18  2024
3   2024-07-18 12:37:22 User: 박지성 Action: Login ID... 2024-07-18  2024
4   2024-07-18 12:38:44 User: 최강타 Action: Purchase... 2024-07-18  2024
5   2024-07-18 12:39:50 User: 장보고 Action: Logout T... 2024-07-18  2024
6   2024-07-18 12:40:56 User: 홍길동 Action: Purchase... 2024-07-18  2024
7   2024-07-18 12:41:00 User: 김철수 Action: Login ID... 2024-07-18  2024
8   2024-07-18 12:42:10 User: 이영희 Action: Purchase... 2024-07-18  2024
9   2024-07-18 12:43:22 User: 박지성 Action: Logout T... 2024-07-18  2024
10  2024-07-18 12:44:44 User: 최강타 Action: Login ID... 2024-07-18  2024
11  2024-07-18 12:45:50 User: 장보고 Action: Purchase... 2024-07-18  2024
12  2024-07-18 12:46:56 User: 홍길동 Action: Logout T... 2024-07-18  2024
13  2024-07-18 12:47:00 User: 김철수 Action: Purchase... 2024-07-18  2024
14  2024-07-18 12:48:10 User: 이영희 Action: Login ID... 2024-07-18  2024
15  2024-07-18 12:49:22 User: 박지성 Action: Purchase... 2024-07-18  2024
16  2024-07-18 12:50:44 User: 최강타 Action: Logout T... 2024-07-18  2024
17  2024-07-18 12:51:50 User: 장보고 Action: Login ID... 2024-07-18  2024
18  2024-07-18 12:52:56 User: 홍길동 Action: Purchase... 2024-07-18  2024
19  2024-07-18 12:53:00 User: 김철수 Action: Logout T... 2024-07-18  2024
20  2024-07-18 12:54:10 User: 이영희 Action: Purchase... 2024-07-18  2024
21  2024-07-18 12:55:22 User: 박지성 Action: Login ID... 2024-07-18  2024
22  2024-07-18 12:56:44 User: 최강타 Action: Purchase... 2024-07-18  2024
23  2024-07-18 12:57:50 User: 장보고 Action: Logout T... 2024-07-18  2024
24  2024-07-18 12:58:56 User: 홍길동 Action: Login ID... 2024-07-18  2024
25  2024-07-18 12:59:00 User: 김철수 Action: Purchase... 2024-07-18  2024
26  2024-07-18 13:00:10 User: 이영희 Action: Logout T... 2024-07-18  2024
27  2024-07-18 13:01:22 User: 박지성 Action: Purchase... 2024-07-18  2024
28  2024-07-18 13:02:44 User: 최강타 Action: Login ID... 2024-07-18  2024
29  2024-07-18 13:03:50 User: 장보고 Action: Purchase... 2024-07-18  2024
'''

#10
df2['시간정보']=df2['로그'].str.extract(r'([0-9]{2}:[0-9]{2}:[0-9]{2})')
print(df2.head())
#11
df2['이름']=df2['로그'].str.extract(r'([가-힣]+)')
print(df2.head())
#12
df2['특수문자_제거_로그']=df2['로그'].str.replace(r'([^가-힣a-zA-Z0-9\s])','',regex=True)
print(df2.head())

#13
df2['user']=df2['로그'].str.extract(r'User:\s*([가-힣]+)')
df2['Amount'] = df2['로그'].str.extract(r'Amount:\s*([0-9]+)').astype(float)

print(df2.head())
'''
df['Amount'] = df['로그'].str.extract(r'Amount:\s*(\d+)').astype(float)
df['User'] = df['로그'].str.extract(r'User:\s*([가-힣]+)')
'''
grouped_df2=df2.groupby('user')['Amount'].mean().reset_index()
print(grouped_df2)
'''
  user       Amount
0  김철수  3666.666667
1  박지성  5750.000000
2  이영희  4250.000000
3  장보고  5750.000000
4  최강타  3750.000000
5  홍길동  4250.000000
'''