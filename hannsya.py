import streamlit as st
import time
import random

st.title("⚡ 反射神経ゲーム")

# セッション状態の初期化
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "waiting" not in st.session_state:
    st.session_state.waiting = False
if "result" not in st.session_state:
    st.session_state.result = None

# ゲーム開始
if st.button("ゲーム開始"):
    st.session_state.result = None
    st.session_state.waiting = True
    wait_time = random.uniform(1, 4)  # 1〜4秒のランダム待ち
    time.sleep(wait_time)
    st.session_state.start_time = time.time()
    st.session_state.waiting = False
    st.rerun()

# 光ったら押すボタン
if st.session_state.start_time and not st.session_state.waiting:
    if st.button("今だ！クリック！"):
        reaction = (time.time() - st.session_state.start_time) * 1000
        st.session_state.result = reaction
        st.session_state.start_time = None
        st.rerun()

# 結果表示
if st.session_state.result:
    st.success(f"反応速度: {st.session_state.result:.1f} ms")
