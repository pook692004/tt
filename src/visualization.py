import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df):
    """Vẽ biểu đồ heatmap để thể hiện mối quan hệ giữa các biến"""
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Biểu đồ tương quan giữa các biến")
    plt.show()
