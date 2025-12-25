import streamlit as st

st.title("🧠 4択クイズゲーム")

# クイズデータ
quiz = [
    {
        "question": "地球で一番大きい動物は？",
        "choices": ["アフリカゾウ", "シロナガスクジラ", "キリン", "ホッキョクグマ"],
        "answer": "シロナガスクジラ"
    },
    {
        "question": "日本の首都は？",
        "choices": ["大阪", "京都", "東京", "名古屋"],
        "answer": "東京"
    },
    {
        "question": "1 + 1 = ?",
        "choices": ["1", "2", "3", "4"],
        "answer": "2"
    }
]

# セッション状態
if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

# ゲーム終了
if st.session_state.finished:
    st.success(f"クイズ終了！あなたのスコアは {st.session_state.score} / {len(quiz)}")
    if st.button("もう一度遊ぶ"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()
    st.stop()

# 現在の問題
q = quiz[st.session_state.index]

st.write(f"**問題 {st.session_state.index + 1} / {len(quiz)}**")
st.write(q["question"])

choice = st.radio("選択肢", q["choices"])

if st.button("回答する"):
    if choice == q["answer"]:
        st.success("正解！")
        st.session_state.score += 1
    else:
        st.error(f"不正解… 正解は「{q['answer']}」")

    st.session_state.index += 1

    if st.session_state.index >= len(quiz):
        st.session_state.finished = True

    st.rerun()
