import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

mpg = sns.load_dataset('mpg')
print(mpg.info())
# mpg = mile per gallon
mpg.dropna(inplace=True)        #결측치가 있는 열 제거

mpg.drop(['name'], axis= 1, inplace=True)
mpg = pd.get_dummies(mpg, columns=['origin'],drop_first=True)       #원 핫 인코딩
# print(mpg.info())

# 독립 변수
x = mpg.drop(['mpg'], axis= 1) #레이블 제거
y = mpg['mpg']      #레이블

print(x.dtypes)   #각 열의 데이터 타입 확인