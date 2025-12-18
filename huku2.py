import streamlit as st

st.title("無料版AIスタイリスト 👕")

age = st.number_input("年齢を入力してください", min_value=10, max_value=100, step=1)
gender = st.selectbox("性別を選んでください", ["男性", "女性", "その他"])
style_pref = st.text_input("好きなスタイル（例：カジュアル、フォーマル、ストリート）")
occasion = st.text_input("服を着るシーン（例：デート、仕事、旅行）")

if st.button("おすすめコーデを生成"):
    # 簡易ルールベース提案
    outfit = f"{age}歳 {gender}向けの{style_pref}スタイル。シーンは{occasion}。"
    if style_pref.lower() == "カジュアル":
        outfit += " ジーンズとシンプルなTシャツ、スニーカーがおすすめです。"
    elif style_pref.lower() == "フォーマル":
        outfit += " スーツやジャケット、革靴が似合います。"
    else:
        outfit += " 個性的なアイテムを組み合わせてみましょう。"
    
    st.subheader("おすすめコーディネート")
    st.write(outfit)
