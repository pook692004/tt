import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def predict_temperature(df):
    """Dự đoán nhiệt độ trung bình toàn cầu vào năm 2050"""
    df['year'] = df['dt'].dt.year
    yearly_avg = df.groupby('year')['AverageTemperature'].mean().dropna()

    X = np.array(yearly_avg.index).reshape(-1, 1)
    y = np.array(yearly_avg.values).reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)
    
    future_years = np.array(range(2025, 2051)).reshape(-1, 1)
    predictions = model.predict(future_years)

    plt.figure(figsize=(10, 5))
    plt.scatter(X, y, label="Dữ liệu thực tế", color='blue')
    plt.plot(future_years, predictions, label="Dự đoán", color='red', linestyle="dashed")
    plt.xlabel("Năm")
    plt.ylabel("Nhiệt độ (°C)")
    plt.title("Dự đoán nhiệt độ trung bình toàn cầu đến năm 2050")
    plt.legend()
    plt.show()

    return predictions

if __name__ == "__main__":
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv", parse_dates=['dt'])
    predict_temperature(df)
