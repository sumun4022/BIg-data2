import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

mpg = sns.load_dataset('mpg')
print(mpg.info())
# mpg = mile per gallon
mpg.dropna(inplace=True)        #결측치가 있는 열 제거
print(mpg.info())
print(mpg)
print(mpg.describe())
