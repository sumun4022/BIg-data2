import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 성별에 따른 생존율 계산
titanic = sns.load_dataset('titanic')
# print(titanic['sex'].head())
gender_survived = titanic.groupby(by='sex')['survived'].mean()
print(gender_survived)

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
