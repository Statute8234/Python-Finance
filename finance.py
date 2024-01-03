import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import random

today = str(date.today())
symbols_lest = ['GOOGL','AMZN','AAPL','TSLA','NVDA','MSFT',]
symbol = random.choice(symbols_lest)

stock_data = yf.download(symbol, start='2021-01-01', end=today)
df = pd.DataFrame(stock_data)
X = df[['High', 'Low', 'Close', 'Adj Close']]
y = df['Volume']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=50)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
normalized_predictions = (predictions - min(predictions)) / (max(predictions) - min(predictions))
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r_squared = r2_score(y_test, predictions)
residuals = y_test - predictions
coefficients = model.coef_
print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
print(f'R-squared: {r_squared}')
print(f'Coefficients: {coefficients}')


x_values = pd.date_range('2022-01-01', periods=len(predictions))
y_values = y_test
color_values = predictions
colormap = plt.cm.get_cmap('RdYlGn')
scatter = plt.scatter(x_values, y_values, c=color_values, cmap=colormap, marker='o')
cbar = plt.colorbar(scatter, label='Actual Value')

plt.title(f"{symbol}")
plt.xlabel('Time')
plt.ylabel('Predictions')
plt.show()

