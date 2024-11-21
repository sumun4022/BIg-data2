import seaborn as sns
import numpy as np

titanic = sns.load_dataset('titanic')
# print(titanic.describe())
# print(titanic.head())
# print(titanic.tail(10))
# print(titanic.info())
# 결측값 처리 방법
# 1. 비어있는 값이 있는 열을 다 지우고 남은 열로만 하는것
# 2. 비어있는 값이 있는 카테고리 전체를 지우는 것
# 3. 비어있는 값을 채워져 있는 값의 평균이나 중간값으로 채우는것
# 4. 비어있는 값을 unknown으로 채우는 것
titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
titanic['deck'].fillna('Unknown', inplace=True)
print(titanic['deck'])
print(titanic.info())