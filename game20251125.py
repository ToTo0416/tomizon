import random
import time
import os

# 画面クリア（Windows / Mac / Linux 対応）
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ゲーム設定
width = 20
player_pos = width // 2
star_pos = random.randint(0, width - 1)
score = 0

while True:
    clear()
    print("=== 落ち物キャッチゲーム ===")
    print("左右キー: a ← / d →   終了: q")
    print(f"スコア: {score}")
    print()

    # ★の表示
    print(" " * star_pos + "★")

    # プレイヤーの表示
    print(" " * player_pos + "▲")

    # 入力受付
    cmd = input("操作: ")

    if cmd == "a" and player_pos > 0:
        player_pos -= 1
    elif cmd == "d" and player_pos < width - 1:
        player_pos += 1
    elif cmd == "q":
        print("ゲーム終了！")
        break

    # ★が落ちる
    if star_pos == player_pos:
        score += 1
        star_pos = random.randint(0, width - 1)
    else:
        # 外したら位置だけ更新
        star_pos = random.randint(0, width - 1)

    time.sleep(0.1)
