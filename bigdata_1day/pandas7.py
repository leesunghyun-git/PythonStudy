import pandas as pd

data = {
'가전제품':['냉장고','세탁기','전자레인지','에어컨','청소기'],
'브랜드':['LG','Samsung','Panasonic','Daikin','Dyson']
}
df=pd.DataFrame(data)

df['제품명_길이']=df['가전제품'].str.len()

df['브랜드_길이']=df['브랜드'].str.len()

print(df)
'''
    가전제품        브랜드  제품명_길이  브랜드_글이
0    냉장고         LG       3       2
1    세탁기    Samsung       3       7
2  전자레인지  Panasonic       5       9
3    에어컨     Daikin       3       6
4    청소기      Dyson       3       5
'''

df['브랜드_소문자']=df['브랜드'].str.lower()
df['브랜드_대문자']=df['브랜드'].str.upper()

print(df[['브랜드','브랜드_소문자','브랜드_대문자']])
'''
         브랜드    브랜드_소문자    브랜드_대문자
0         LG         lg         LG
1    Samsung    samsung    SAMSUNG
2  Panasonic  panasonic  PANASONIC
3     Daikin     daikin     DAIKIN
4      Dyson      dyson      DYSON
'''

#문자열 포함 여부

df['브랜드에_a_포함']=df['브랜드'].str.contains('a')

print(df[['브랜드','브랜드에_a_포함']])
'''
         브랜드  브랜드에_a_포함
0         LG      False
1    Samsung       True
2  Panasonic       True
3     Daikin       True
4      Dyson      False
'''

df['브랜드_언더스코어']=df['브랜드'].str.replace('L','HHHHG')

print(df[['브랜드','브랜드_언더스코어']])

'''
         브랜드  브랜드_언더스코어
0         LG     HHHHGG
1    Samsung    Samsung
2  Panasonic  Panasonic
3     Daikin     Daikin
4      Dyson      Dyson
'''

#문자열 분할

df[['브랜드_첫부분','브랜드_두번째','브랜드_세번째']]=df['브랜드'].str.split('a',expand=True)

print(df[['브랜드','브랜드_첫부분','브랜드_두번째','브랜드_세번째']])

'''
         브랜드 브랜드_첫부분 브랜드_두번째 브랜드_세번째
0         LG      LG    None    None
1    Samsung       S   msung    None
2  Panasonic       P       n   sonic
3     Daikin       D    ikin    None
4      Dyson   Dyson    None    None
'''

df['제품_브랜드']=df['가전제품'].str.cat(df['브랜드'],sep=',')

print(df[['가전제품','브랜드','제품_브랜드']])
'''
    가전제품        브랜드           제품_브랜드
0    냉장고         LG           냉장고,LG
1    세탁기    Samsung      세탁기,Samsung
2  전자레인지  Panasonic  전자레인지,Panasonic
3    에어컨     Daikin       에어컨,Daikin
4    청소기      Dyson        청소기,Dyson
'''

df['가전제품']=df['가전제품'].str.replace('전자레인지','    전자레인지       ')
df['가전제품_공백제거']=df['가전제품'].str.strip()

print(df[['가전제품','가전제품_공백제거']])