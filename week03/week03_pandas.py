import pandas as pd

def square(n) -> int:
    return n * n

# df = pd.DataFrame(
#     {
#     "a": [14,51,6],
#     "b": [72, 8, 72],
#     "c": [100, 11, 12]
#     }, index = [1, 2, 3]
# )
df = pd.DataFrame(
    [
        [14,72,100],
        [51, 8, 11],
        [6, 72, 12]
    ], index = [1, 2, 3], columns=["a", "b","c"]
)
print(df)
df2 = df.melt().rename(columns={'variable':'var','value':'val'})        #melt로 출력한 데이터의 열의 이름을 다른 이름으로 변경한다.
df3 = df.melt().rename(columns={'variable':'var','value':'val'}).query('val >= 10')       #melt로 출력한 데이터중 val의 값이 15 초과인 값의 행만 출력한다.
df4 = (df.melt().rename(columns={'variable':'var','value':'val'}).query('val >= 10')
       .sort_values('val',ascending=False))     #해당 열의 데이터를 정렬하는 함수이다. true면 오름차순, false면 내림차순이다.
# print(df.iloc[1:2])           #데이터 프레임의 숫자를 통해 데이터를 가져온다.
# print(df.loc[1,'a'])
print(df.loc[:,'a'])            #데이터 프레임의 행, 열의 이름을 통해 데이터를 가져온다.
print(df.apply(square))             #함수를 데이터 프레임에 적용할 수 있게 해주는 함수이다.
print(df4)
# print(df.melt())            #데이터를 긴 형태로 보여준다.(모든 데이터를 두개의 열로 보여준다.)
print(df.shape)
print(df["a"].mean())       #해당 열에 있는 모든 숫자의 평균을 타나낸다.
print(df.mean())            #각 열에 있는 숫자들의 평균값을 나타낸다.
bb = "a"
min_max = "최대값"
print(f'{bb}열의 {min_max} : {df[bb].max()}')     #min,max는 해당 열에서 최대, 최소값을 구한다.(열을 넣지 않고 df.min,df.max를 사용하면 모든 열에서 구한다.)
# print(df["c"].value_counts())
print(df["b"].nunique())       #df["b"].nunique()는 해당 열의 고유 값의 숫자를 나타낸다.(즉, 해당 열에 있는 중복되지 않는 데이터를 의미한다.)
                                #df.nunique() 이렇게 사용하면 모든 데이터프레임의 각 열에 있는 고유값 개수를 보여준다.
print(df.describe())        #describe은 데이터의 통계를 나타낸다.
print(df.nunique())
# 데이터 프레임 구조는 두가지로 만들 수 있다.

ds = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(ds)