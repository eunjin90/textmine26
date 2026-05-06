import streamlit as st
import time

@st.cache_data
def change_text():
    text = st.title('텍스트가 변할 겁니다')
    time.sleep(3)
    text = text.info('3초가 지났습니다.')

change_text()
'바꿔보자'