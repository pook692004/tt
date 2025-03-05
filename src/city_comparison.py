import pandas as pd
import matplotlib.pyplot as plt

def compare_cities(df, cities):
    """So sánh nhiệt độ trung bình của các thành phố theo thời gian"""
    df['year'] = df['dt'].dt.year
    city_avg = df[df['City'].isin(cities)].groupby(['year', 'City'])['AverageTemperature'].mean().unstack()

    plt.figure(figsize=(10, 5))
    city_avg.plot()
    plt.xlabel("Năm")
    plt.ylabel("Nhiệt độ (°C)")
    plt.title("So sánh nhiệt độ trung bình giữa các thành phố")
    plt.legend(title="Thành phố")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv", parse_dates=['dt'])
    compare_cities(df, ["New York", "London", "Tokyo", "Sydney"])
