from data_loader import load_data
from data_preprocessing import preprocess_data
from trend_analysis import analyze_global_trend
from city_comparison import compare_cities

from advanced_prediction import predict_temperature_multiple_models

def main():
    # Tải dữ liệu
    df = load_data("data/GlobalLandTemperaturesByCity.csv")

    # Tiền xử lý
    df = preprocess_data(df)

    # Phân tích xu hướng nhiệt độ trung bình toàn cầu
    analyze_global_trend(df)

    # So sánh nhiệt độ giữa các thành phố
    compare_cities(df, ["New York", "London", "Tokyo", "Sydney"])

    predict_temperature_multiple_models(df)

if __name__ == "__main__":
    main()
