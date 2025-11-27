import streamlit as st 

st.title("こんにちわ、吉村ゼミ")

name = st.test_input("好きな言葉を入力してください")
st.write(name) 

st.checkbox("同意します") 
address = st.selectbox("次の中から現住所を教えて",["京都府","大阪府"])
st.write(address)
hobby = st.multiselect("趣味を次から選択して",["映画","音楽","散歩"])
st.write(hobby)

st.slider("この映画を10点満点で評価してください"0,10,0")
st.write(score)
st.radio("性別を選択してください"["男性","女性"])
list =[
{"latitude":30.05,"longitude":135.76},
{"latitude":35.04,"longtude":135.75},
]
st.map(list)
camera_photo = st.camera_input("写真を撮影します")
if camera:
  st.image(camera,caption="写真",use_column_width=true)
