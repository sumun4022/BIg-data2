import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values
# Visualize the data
lifesat.plot(kind='scatter', grid=True,
x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23500, 62500, 4, 9])
plt.show()
# Select a linear model
model = KNeighborsRegressor(n_neighbors=3) # K 최근접 모델 사용
# Train the model
model.fit(X, y)
# Make a prediction for Cyprus
X_new = [[37655.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.30165767]]