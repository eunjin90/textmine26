import NaverNewsCrawler as nnc
import streamlit as st

st.title("네이버 뉴스 수집기")

# Streamlit 입력창 사용 (input() 대신 st.text_input 사용)
keyword = st.text_input('검색할 키워드를 입력하세요 : ')

if keyword:
    # nnc 모듈을 사용하여 뉴스 100개 수집
    corpus = nnc.crawl_naver_news_all(keyword)
    
    st.write(f"수집된 뉴스 개수: {len(corpus)}개")
    
    # 상위 3개 뉴스 본문(description) 출력 테스트
    if len(corpus) > 0:
        st.subheader("최근 뉴스 미리보기")
        for news in corpus[:3]:
            # HTML 태그 제거 없이 그대로 출력
            st.write(f"- {news['title']}")