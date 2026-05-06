import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def visualize_barh_graph(counter, num_word):
    # 상위 N개 데이터 추출
    top_words = counter.most_common(num_word)
    words, counts = zip(*top_words)
    
    fig, ax = plt.subplots() # subplot() -> subplots() 수정
    ax.barh(words, counts)
    ax.invert_yaxis() # 높은 순서가 위로 오게
    st.pyplot(fig)

def visualize_wordcloud(counter, num_word):
    # 빈도수 기반 워드클라우드 생성
    wc = WordCloud(
        font_path='malgun',
        background_color='white',
        width=800, height=600
    ).generate_from_frequencies(counter)
    
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)