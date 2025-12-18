def recommend_outfit(temp, weather):
    outfit = []

    # 気温に応じた服装
    if temp < 5:
        outfit.append("ダウンジャケット")
        outfit.append("手袋とマフラー")
    elif temp < 15:
        outfit.append("コート")
        outfit.append("長袖シャツ")
    elif temp < 25:
        outfit.append("カーディガン")
        outfit.append("薄手の長袖")
    else:
        outfit.append("Tシャツ")
        outfit.append("ショートパンツ")

    # 天気に応じたアイテム
    if "雨" in weather or "雪" in weather:
        outfit.append("傘")
        if "雪" in weather:
            outfit.append("防水ブーツ")
        else:
            outfit.append("レインコート")

    return outfit

# ユーザー入力
try:
    temp = float(input("気温を入力してください（例：18.5）: "))
    weather = input("天気を入力してください（例：晴れ、雨、曇り、雪）: ")

    outfit = recommend_outfit(temp, weather)
    print("\nおすすめの服装:")
    for item in outfit:
        print(f"- {item}")
except ValueError:
    print("数字で気温を入力してね！")
