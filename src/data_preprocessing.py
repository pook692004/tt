import pandas as pd

def preprocess_data(df):
    """Tiền xử lý dữ liệu nhiệt độ toàn cầu"""
    
    # Tạo một bản sao của DataFrame để tránh lỗi SettingWithCopyWarning
    df = df.dropna(subset=['AverageTemperature']).copy()

    # Chuyển đổi cột 'dt' thành kiểu datetime
    df['dt'] = pd.to_datetime(df['dt'], errors='coerce')

    # Thêm cột 'year' để phân tích xu hướng
    df['year'] = df['dt'].dt.year

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv")
    df = preprocess_data(df)
    print(df.head())
