import streamlit as st

st.title("🧠 カテゴリ選択式クイズゲーム")

# クイズデータ
quiz_data = {
    "一般常識": [
        {
            "q": "日本の国鳥は？",
            "choices": ["キジ", "スズメ", "ツル", "タカ"],
            "a": "キジ"
        },
        {
            "q": "太陽に一番近い惑星は？",
            "choices": ["金星", "地球", "水星", "火星"],
            "a": "水星"
        }
    ],
    "数学": [
        {
            "q": "√49 は？",
            "choices": ["5", "6", "7", "8"],
            "a": "7"
        },
        {
            "q": "3×4＋2 の答えは？",
            "choices": ["10", "12", "14", "20"],
            "a": "14"
        }
    ],
    "英語": [
        {
            "q": "apple の意味は？",
            "choices": ["バナナ", "リンゴ", "机", "犬"],
            "a": "リンゴ"
        },
        {
            "q": "blue の意味は？",
            "choices": ["赤", "青", "黄色", "白"],
            "a": "青"
        }
    ]
}

# セッション状態
if "category" not in st.session_state:
    st.session_state.category = None
if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

# カテゴリ選択
if st.session_state.category is None:
    st.write("クイズのカテゴリを選んでください")
    category = st.selectbox("カテゴリ", list(quiz_data.keys()))

    if st.button("スタート"):
        st.session_state.category = category
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()

else:
    # 選んだカテゴリの問題を取得
    quiz_list = quiz_data[st.session_state.category]

    # 終了判定
    if st.session_state.finished:
        st.success(f"終了！スコア：{st.session_state.score} / {len(quiz_list)}")
        if st.button("もう一度カテゴリ選択へ"):
            st.session_state.category = None
            st.rerun()
        st.stop()

    # 現在の問題
    q = quiz_list[st.session_state.index]

    st.write(f"カテゴリ：**{st.session_state.category}**")
    st.write(f"問題 {st.session_state.index + 1} / {len(quiz_list)}")
    st.write(q["q"])

    choice = st.radio("選択肢", q["choices"])

    if st.button("回答する"):
        if choice == q["a"]:
            st.success("正解！")
            st.session_state.score += 1
        else:
            st.error(f"不正解… 正解は「{q['a']}」")

        st.session_state.index += 1

        if st.session_state.index >= len(quiz_list):
            st.session_state.finished = True

        st.rerun()
