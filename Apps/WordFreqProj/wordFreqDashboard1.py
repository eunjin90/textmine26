import mylib.myTextMining as ta
import streamlit as st
import mylib.mySTVisualizer as sv
from konlpy.tag import Okt

st.title("영화 리뷰 텍스트 마이닝 대시보드") # 제목 확인

# 영화 리뷰 데이터 경로
datafile = "./data/daum_movie_review.csv"

# 1. 데이터 준비
corpus = ta.load_corpus(datafile, 'review')

# 2. 빈도수 만들기
my_tags = ['Noun', 'Verb', 'Adjective']
my_stopwords = ['은', '는', '이', '가', '을', '를', '의', '에']
counter = ta.count_word_freq(corpus, Okt().pos, my_tags, my_stopwords)

# 3. 그래프와 워드클라우드 출력
st.subheader("단어 빈도수 TOP 20")
sv.visualize_barh_graph(counter, 20)

st.subheader("워드클라우드")
sv.visualize_wordcloud(counter, 50)