import streamlit as st
import random
from PIL import Image, ImageDraw

st.set_page_config(page_title="Outfit Recommendation", layout="wide")
st.title("Content-Based Outfit Recommendation")

# -----------------------------
# 0. Gender / Height / Body Type
# -----------------------------
gender = st.radio("性別を選択してください", ["男性", "女性"])
height_type = st.selectbox("身長タイプを選択", ["低い", "普通", "高い"])
body_type = st.selectbox("骨格タイプを選択", ["ストレート", "ウェーブ", "ナチュラル"])

# -----------------------------
# 1. Genre & Color Definitions
# -----------------------------

GENRES = [
    "Streetwear",
    "Casual",
    "Minimal",
    "Techwear",
    "Vintage",
    "Formal"
]

COLORS = [
    "Black",
    "White",
    "Gray",
    "Navy",
    "Brown",
    "Beige",
    "Green",
    "Red"
]

COLOR_RGB = {
    "Black": (30, 30, 30),
    "White": (240, 240, 240),
    "Gray": (160, 160, 160),
    "Navy": (40, 60, 100),
    "Brown": (120, 80, 50),
    "Beige": (210, 200, 170),
    "Green": (60, 120, 80),
    "Red": (160, 50, 50)
}

# -----------------------------
# 2. User Input
# -----------------------------

st.header("1️⃣ スタイルの好みを 0〜5 で評価")

genre_scores = {}
for g in GENRES:
    genre_scores[g] = st.slider(g, 0, 5, 0)

st.header("2️⃣ 色の好みを 0〜5 で評価")

color_scores = {}
for c in COLORS:
    color_scores[c] = st.slider(c, 0, 5, 0)

# -----------------------------
# 3. Score Completion
# -----------------------------

def complete_scores(scores: dict):
    if all(v == 0 for v in scores.values()):
        return {k: 3 for k in scores}  # デフォルト値
    return scores

genre_scores = complete_scores(genre_scores)
color_scores = complete_scores(color_scores)

# -----------------------------
# 4. Select Top Genres & Colors
# -----------------------------

top_genres = sorted(genre_scores, key=genre_scores.get, reverse=True)[:3]
top_colors = sorted(color_scores, key=color_scores.get, reverse=True)[:3]

# -----------------------------
# 5. Outfit Templates (Gender-Specific)
# -----------------------------

OUTFIT_LIBRARY_MALE = {
    "Streetwear": {
        "inner": ["Graphic Tee", "Long Sleeve Tee"],
        "outer": ["Hoodie", "Zip Hoodie"],
        "bottom": ["Cargo Pants", "Wide Pants"]
    },
    "Casual": {
        "inner": ["Plain T-Shirt", "Knit"],
        "outer": ["Cardigan", "Light Jacket"],
        "bottom": ["Denim", "Chinos"]
    },
    "Minimal": {
        "inner": ["Plain Tee"],
        "outer": ["Tailored Jacket"],
        "bottom": ["Slim Slacks"]
    },
    "Techwear": {
        "inner": ["Functional Tee"],
        "outer": ["Shell Jacket"],
        "bottom": ["Tech Pants"]
    },
    "Vintage": {
        "inner": ["Retro Tee"],
        "outer": ["Denim Jacket"],
        "bottom": ["Straight Jeans"]
    },
    "Formal": {
        "inner": ["Dress Shirt"],
        "outer": ["Blazer"],
        "bottom": ["Slacks"]
    }
}

OUTFIT_LIBRARY_FEMALE = {
    "Streetwear": {
        "inner": ["Crop Tee", "Long Sleeve Tee"],
        "outer": ["Oversized Hoodie", "Zip Hoodie"],
        "bottom": ["Cargo Pants", "Wide Pants", "Skirt"]
    },
    "Casual": {
        "inner": ["Blouse", "Knit"],
        "outer": ["Cardigan", "Light Jacket"],
        "bottom": ["Denim", "Skirt", "Wide Pants"]
    },
    "Minimal": {
        "inner": ["Plain Tee", "Blouse"],
        "outer": ["Tailored Jacket"],
        "bottom": ["Slim Pants", "Skirt"]
    },
    "Techwear": {
        "inner": ["Functional Tee"],
        "outer": ["Shell Jacket"],
        "bottom": ["Tech Pants"]
    },
    "Vintage": {
        "inner": ["Retro Blouse"],
        "outer": ["Denim Jacket"],
        "bottom": ["Straight Jeans", "Skirt"]
    },
    "Formal": {
        "inner": ["Blouse"],
        "outer": ["Blazer"],
        "bottom": ["Slacks", "Skirt"]
    }
}

OUTFIT_LIBRARY = OUTFIT_LIBRARY_MALE if gender == "男性" else OUTFIT_LIBRARY_FEMALE

# -----------------------------
# 6. Outfit Generator
# -----------------------------

def generate_outfit(genre, color):
    parts = OUTFIT_LIBRARY[genre]
    return {
        "Genre": genre,
        "Color Theme": color,
        "Inner": f"{color} {random.choice(parts['inner'])}",
        "Outer": f"{color} {random.choice(parts['outer'])}",
        "Bottom": f"{color} {random.choice(parts['bottom'])}"
    }

# -----------------------------
# 7. Image Generator (Gender + Height + Body Type)
# -----------------------------

def generate_image(outfit, gender, height_type, body_type):
    base_color = COLOR_RGB[outfit["Color Theme"]]

    img = Image.new("RGB", (260, 440), (245, 245, 245))
    d = ImageDraw.Draw(img)

    # 身長倍率
    if height_type == "低い":
        h = 0.9
    elif height_type == "普通":
        h = 1.0
    else:
        h = 1.12  # 少し長め

    # 骨格による肩幅・ウエスト幅
    if body_type == "ストレート":
        shoulder = 140
        waist = 110
    elif body_type == "ウェーブ":
        shoulder = 120
        waist = 90
    else:  # ナチュラル
        shoulder = 150
        waist = 120

    # 性別補正
    if gender == "男性":
        shoulder += 10
        waist += 10
    else:
        waist -= 10

    # 座標補助
    def Y(y):
        return int(y * h)

    skin = (220, 200, 180)
    inner_color = tuple(min(255, c + 35) for c in base_color)
    bottom_color = tuple(max(0, c - 50) for c in base_color)

    # Head
    d.ellipse([105, Y(20), 155, Y(70)], fill=skin, outline="black")

    # Neck
    d.rectangle([120, Y(70), 140, Y(95)], fill=skin)

    # Torso (shoulders → waist)
    d.polygon([
        (130 - shoulder//2, Y(100)),
        (130 + shoulder//2, Y(100)),
        (130 + waist//2, Y(250)),
        (130 - waist//2, Y(250))
    ], fill=base_color, outline="black")

    # Inner
    d.rectangle([95, Y(120), 165, Y(250)], fill=inner_color, outline="black")

    # Bottom (legs)
    d.rectangle([110, Y(250), 130, Y(400)], fill=bottom_color, outline="black")
    d.rectangle([130, Y(250), 150, Y(400)], fill=bottom_color, outline="black")

    # Shoes
    d.rectangle([110, Y(400), 130, Y(420)], fill=(40, 40, 40))
    d.rectangle([130, Y(400), 150, Y(420)], fill=(40, 40, 40))

    return img

# -----------------------------
# 8. Generate 3 Outfits
# -----------------------------

st.header("👕 Recommended Outfits")

used_colors = []

for i, genre in enumerate(top_genres):
    color = random.choice(top_colors)

    if color in used_colors and len(top_colors) > 1:
        color = random.choice([c for c in top_colors if c not in used_colors])

    used_colors.append(color)

    outfit = generate_outfit(genre, color)
    img = generate_image(outfit, gender, height_type, body_type)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.image(img, caption=f"Outfit {i+1}")

    with col2:
        st.subheader(f"Outfit {i+1} Details")
        st.write(f"**Genre:** {outfit['Genre']}")
        st.write(f"**Color Theme:** {outfit['Color Theme']}")
        st.write(f"👕 Inner: {outfit['Inner']}")
        st.write(f"🧥 Outer: {outfit['Outer']}")
        st.write(f"👖 Bottom: {outfit['Bottom']}")

# -----------------------------
# 9. Display Final Scores
# -----------------------------

st.header("📊 Final Recommendation Scores")

st.subheader("Genre Scores")
st.json(genre_scores)

st.subheader("Color Scores")
st.json(color_scores)
