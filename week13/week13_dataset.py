import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
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

# print(x.dtypes)   #각 열의 데이터 타입 확인

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

#결과 출력
print(f"mse : {mse}")
print(f"r2_score : {r2}")


#시각화
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, color='aqua', alpha=0.6)
plt.plot([y.min(),y.max()], [y.min(),y.max()], color='red', linestyle='--')
plt.title('actual data vs predict data')
plt.xlabel('actual MPG')
plt.ylabel('predict MPG')
plt.grid(True)
plt.show()