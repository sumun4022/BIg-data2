import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# age_survived = titanic.groupby(by='age')['survived'].mean()
# # print(age_survived)
# plt.hist(age_survived, color='green')
# plt.title('Survival Rate by age')
# plt.xlabel('age')
# plt.ylabel('survived Rate')
# plt.show()

# 나이에 따른 생존율 계산
# 1. 결측치 행 제거
titanic_drop = titanic.dropna(subset=['age'])
# print(titanic_drop.info())
# 2. 생존율 계산
titanic_drop['survived'] = titanic_drop['survived'].astype(float)
# print(titanic_drop['survived'])
plt.figure(figsize=(10,5))
sns.histplot(data=titanic_drop, x='age', weights='survived', bins=30, kde=False)
plt.title('survival Rate by age (Dropna)')
plt.xlabel('Age')
plt.ylabel('survival Rate (weights)')
plt.show()

# 성별에 따른 생존율 계산
# print(titanic['sex'].head())
# gender_survived = titanic.groupby(by='sex')['survived'].mean()
# print(type(gender_survived)) #<class 'pandas.core.series.Series'>

# gender_survived = titanic.groupby(by='sex')['survived'].mean().reset_index()
# print(type(gender_survived)) #<class 'pandas.core.series.Series'>
# sns.barplot(data=gender_survived, x='sex', y='survived')
# plt.title('Survival Rate by gender')
# plt.ylabel('survived Rate')
# plt.show()
# print(gender_survived)
# print(gender_survived.info())


# titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
# titanic['deck'].fillna('Unknown', inplace=True)
# print(titanic['deck'])
# print(titanic.info())

# print(titanic['survived'])

# 생존자와 사망자 수 시각화
# sns.countplot(data=titanic, x='survived')
# plt.title('Survived (0 = no, 1 = yes)')
# plt.xlabel('Survived')
# plt.ylabel('Count')
# plt.show()
