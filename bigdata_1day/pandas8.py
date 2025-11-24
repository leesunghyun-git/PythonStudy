import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_data.csv')
print('----------df.shpae-----------')
print(df.shape)

print('--------df.info----------')
print(df.info())

print('--------df.head()---------')
print(df.head())
'''
----------df.shpae-----------
(435, 12)
--------df.info----------
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
--------df.head()---------
              datetime  season  holiday  workingday  weather   temp   atemp  humidity  windspeed  casual  registered  count
0  2011-09-05 17:00:00       3        1           0        2  27.06  29.545        89     7.0015      37          77    114
1  2011-05-17 11:00:00       2        0           1        2  22.96  26.515        83    27.9993      26         104    130
2  2011-11-10 09:00:00       4        0           1        2  17.22  21.210        94     7.0015      23         188    211
3  2011-10-13 07:00:00       4        0           1        3  22.14  25.760       100     8.9981       5          76     81
4  2011-10-15 14:00:00       4        0           0        1  24.60  31.060        33    31.0009     242         230    472
'''

df['datetime']=pd.to_datetime(df['datetime'])

print(df.info())
'''
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   datetime    435 non-null    datetime64[ns]
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
'''

#1
df['hour']=df['datetime'].dt.hour
df['year']=df['datetime'].dt.year
df['month']=df['datetime'].dt.month
df['day']=df['datetime'].dt.day

print(df.head(2))
'''
             datetime  season  holiday  workingday  weather   temp   atemp  humidity  windspeed  casual  registered  count  hour  year  month  day
0 2011-09-05 17:00:00       3        1           0        2  27.06  29.545        89     7.0015      37          77    114    17  2011      9    5
1 2011-05-17 11:00:00       2        0           1        2  22.96  26.515        83    27.9993      26         104    130    11  2011      5   17
'''

summary_data=df.groupby(['season','hour']).agg({'count':'sum'}).reset_index()

print(summary_data)
'''
    season  hour  count
0        1     0     70
1        1     1    132
2        1     2     65
3        1     3     35
4        1     4      5
..     ...   ...    ...
91       4    19   2519
92       4    20    484
93       4    21    468
94       4    22    595
95       4    23     99

'''

max_count_hour=df.loc[df['count'].idxmax(),'hour']
max_count=df['count'].max()

print(max_count_hour)
print(max_count)
'''
17
970
'''

#2

summary_season_df=df.groupby('season')['count'].mean().reset_index()

print(summary_season_df)
'''
   season       count
0       1  103.169811
1       2  218.803922
2       3  265.500000
3       4  218.581197
'''