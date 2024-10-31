import seaborn as sns
import numpy as np

titanic = sns.load_dataset('titanic')
# print(titanic.describe())
# print(titanic.head())
# print(titanic.tail(10))
print(titanic.info())
# print(titanic['embarked'], titanic['deck'], titanic['class'])