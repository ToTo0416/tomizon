from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# ユーザーの過去の服装データ（気温, 天気コード, 服装リスト）
# 天気コード例: 晴れ=0, 曇り=1, 雨=2, 雪=3
user_history = [
    {"temp": 10, "weather": 2, "outfit": ["コート", "長袖シャツ", "傘"]},
    {"temp": 22, "weather": 0, "outfit": ["Tシャツ", "ジーンズ"]},
    {"temp": 5, "weather": 3, "outfit": ["ダウン", "手袋", "防水ブーツ"]},
    {"temp": 18, "weather": 1, "outfit": ["カーディガン", "長袖シャツ"]},
]

# 天気を数値に変換
weather_map = {"晴れ": 0, "曇り": 1, "雨": 2, "雪": 3}

def recommend_by_similarity(current_temp, current_weather):
    current_vector = np.array([[current_temp, weather_map.get(current_weather, 0)]])
    history_vectors = np.array([[entry["temp"], entry["weather"]] for entry in user_history])

    # 類似度を計算
    similarities = cosine_similarity(current_vector, history_vectors)[0]
    best_match_index = np.argmax(similarities)
    return user_history[best_match_index]["outfit"]

# ユーザー入力
try:
    temp = float(input("気温を入力してね（例：15.0）: "))
    weather = input("天気を入力してね（晴れ、曇り、雨、雪）: ")

    recommended = recommend_by_similarity(temp, weather)
    print("\nおすすめの服装（過去の似た条件から）:")
    for item in recommended:
        print(f"- {item}")
except ValueError:
    print("気温は数字で入力してね！")
