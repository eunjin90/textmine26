import pandas as pd
from collections import Counter

# csv 파일에서 분석 대상 텍스트 추출
def load_corpus(datafile, col_name='review'): # 기본값 'review' 설정
    data_df = pd.read_csv(datafile)
    # 결측치(NaN) 제거 후 리스트 변환
    reviews = list(data_df[col_name].dropna()) 
    return reviews

def tokenize_korean_corpus(corpus, tokenizer, my_tags, my_stopwords):
    words = []
    for review in corpus:
        # 형태소 분석 진행 (stem=True로 원형 추출)
        for word, pos in tokenizer(review, stem=True):
            # 선택한 태그에 해당하고, 불용어가 아니며, 2글자 이상인 단어
            if pos in my_tags and word not in my_stopwords and len(word) > 1:
                words.append(word) # words.append(words) 오타 수정
    return words

# 빈도수 계산 통합 함수
def count_word_freq(corpus, tokenizer, my_tags, my_stopwords):
    # 위에서 정의한 토큰화 함수 호출 (인자 전달 필수)
    tokens = tokenize_korean_corpus(corpus, tokenizer, my_tags, my_stopwords)
    return Counter(tokens)