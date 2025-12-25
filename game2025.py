import streamlit as st
import random

st.title("🎮 数当てゲーム（Streamlit版）")

# セッション状態の初期化
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
if "message" not in st.session_state:
    st.session_state.message = "1〜100の数字を当ててください！"

st.write(st.session_state.message)

# 入力
guess = st.number_input("数字を入力", min_value=1, max_value=100, step=1)

# ボタン
if st.button("判定する"):
    if guess < st.session_state.answer:
        st.session_state.message = "もっと大きい数字です"
    elif guess > st.session_state.answer:
        st.session_state.message = "もっと小さい数字です"
    else:
        st.session_state.message = "🎉 正解！ゲームクリア！"
    st.experimental_rerun()

# リセットボタン
if st.button("リセット"):
    st.session_state.answer = random.randint(1, 100)
    st.session_state.message = "ゲームをリセットしました！"
    st.experimental_rerun()
