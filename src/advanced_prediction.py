import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def predict_temperature_multiple_models(df):
    """Dự đoán nhiệt độ trung bình toàn cầu sử dụng nhiều mô hình khác nhau"""
    df['year'] = df['dt'].dt.year
    yearly_avg = df.groupby('year')['AverageTemperature'].mean().dropna()

    X = np.array(yearly_avg.index).reshape(-1, 1)
    y = np.array(yearly_avg.values)

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Khởi tạo các mô hình
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Support Vector Machine": SVR(kernel='rbf')
    }

    # Huấn luyện và đánh giá các mô hình
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            "model": model,
            "MSE": mse,
            "R²": r2
        }
        
        print(f"{name}: MSE = {mse:.4f}, R² = {r2:.4f}")

    # Dự đoán nhiệt độ tương lai
    future_years = np.array(range(2025, 2051)).reshape(-1, 1)
    
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, label="Dữ liệu thực tế", color='blue', alpha=0.5)
    
    colors = ['red', 'green', 'purple']
    styles = ['--', '-.', ':']
    
    for (name, result), color, style in zip(results.items(), colors, styles):
        model = result["model"]
        predictions = model.predict(future_years)
        plt.plot(future_years, predictions, label=f"Dự đoán ({name})", 
                 color=color, linestyle=style, linewidth=2)
    
    plt.xlabel("Năm")
    plt.ylabel("Nhiệt độ (°C)")
    plt.title("So sánh các mô hình dự đoán nhiệt độ trung bình toàn cầu đến năm 2050")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Vẽ biểu đồ so sánh độ chính xác giữa các mô hình
    plt.figure(figsize=(10, 5))
    metrics = ['MSE', 'R²']
    
    for i, metric in enumerate(metrics):
        plt.subplot(1, 2, i+1)
        values = [result[metric] for result in results.values()]
        plt.bar(list(results.keys()), values, color=['red', 'green', 'purple'])
        plt.title(f"So sánh {metric}")
        plt.xticks(rotation=45)
        if metric == 'MSE':
            plt.ylabel("Mean Squared Error (MSE)")
        else:
            plt.ylabel("R-squared (R²)")
    
    plt.tight_layout()
    plt.show()
    
    return results

if __name__ == "__main__":
    df = pd.read_csv("data/GlobalLandTemperaturesByCity.csv", parse_dates=['dt'])
    predict_temperature_multiple_models(df)