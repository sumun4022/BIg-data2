import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


titanic = sns.load_dataset('titanic')       #데이터 로딩
median_age = titanic['age'].median()
titanic_fill = titanic.fillna({'age': median_age})

X = titanic_fill[['age']]  #독립 변수
y = titanic_fill['survived'] #독립 변수

X_trian, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 선택
model = LogisticRegression()

# 모델 학습
model.fit(X_trian, y_train)

# 예측
y_pred = model.predict(X_test)

# 시각화
plt.figure(figsize=(10,5))
plt.scatter(X_test, y_test, color='blue',label='Actual')
plt.scatter(X_test, y_pred, color='red',label='Predicted', alpha=0.2)
plt.title('Linear Regression: Real vs Predict')
plt.xlabel('Age')
plt.ylabel('survival')
plt.show()