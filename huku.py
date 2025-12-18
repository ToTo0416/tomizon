import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = "YOUR_API_KEY"

st.title("AIパーソナルスタイリスト 👕")

# Step 1: ユーザーに質問
age = st.number_input("年齢を入力してください", min_value=10, max_value=100, step=1)
gender = st.selectbox("性別を選んでください", ["男性", "女性", "その他"])
style_pref = st.text_input("好きなスタイル（例：カジュアル、フォーマル、ストリート）")
occasion = st.text_input("服を着るシーン（例：デート、仕事、旅行）")

if st.button("おすすめコーデを生成"):
    # Step 2: AIに服装を提案させる
    prompt = f"""
    あなたはファッションスタイリストです。
    年齢: {age}
    性別: {gender}
    好み: {style_pref}
    シーン: {occasion}
    この条件に合う服装を具体的に提案してください。
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    outfit_text = response.choices[0].text.strip()
    st.subheader("おすすめコーディネート")
    st.write(outfit_text)

    # Step 3: 画像生成（Stable DiffusionやDALL·Eを利用）
    image_prompt = f"ファッションイラスト: {outfit_text}"
    image_response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="512x512"
    )

    st.image(image_response['data'][0]['url'], caption="AI生成コーディネート")
