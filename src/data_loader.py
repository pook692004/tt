import pandas as pd

def load_data(file_path):
    """Đọc file CSV và trả về DataFrame"""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = load_data("data/GlobalLandTemperaturesByCity.csv")
    print(df.head())
