import pandas as pd
import matplotlib.pyplot as plt

def analyze_global_trend(df):
    """Vẽ biểu đồ xu hướng nhiệt độ trung bình toàn cầu"""
    yearly_avg = df.groupby('year')['AverageTemperature'].mean()

    plt.figure(figsize=(10, 5))
    plt.plot(yearly_avg, label="Nhiệt độ trung bình toàn cầu", color='red')
    plt.xlabel("Năm")
    plt.ylabel("Nhiệt độ (°C)")
    plt.title("Xu hướng nhiệt độ trung bình toàn cầu theo năm")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv", parse_dates=['dt'])
    analyze_global_trend(df)
