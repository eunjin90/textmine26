import mylib.myTextMining as ta     # 텍스트 데이터 처리(파일 로드, 단어 세기) 도구
import streamlit as st              # 웹 화면을 만들어주는 도구
import mylib.mySTVisualizer as sv   # 그래프와 워드클라우드를 그려주는 도구
from konlpy.tag import Okt          # 한글 문장에서 형태소(명사 등)를 추출하는 도구
import requests                     # 특정 웹 주소(URL)에 접속을 요청하는 도구
from bs4 import BeautifulSoup       # 뷰티풀스프 불러오기(HTML 코드에서 텍스트만 뽑아내는 도구)

# --- 사이드바 영역: 사용자가 설정을 조절하는 곳 ---
st.sidebar.header("데이터 소스 선택")   # 사이드바 제목 표시
# 라디오 버튼으로 데이터 가져올 방식 선택 (CSV vs 웹)
source_type = st.sidebar.radio("데이터를 어디서 가져올까요?", ("CSV 파일 업로드", "웹 페이지 긁어오기(BeautifulSoup)"))

corpus = []     # 분석할 문장들을 담을 빈 주머니(리스트) 생성

if source_type == "CSV 파일 업로드":
    # 파일을 마우스로 끌어서 올릴 수 있는 창 생성
    uploaded_file = st.sidebar.file_uploader("CSV 파일을 드래그하여 놓으세요", type=['csv'])
    # CSV 파일 안에서 어떤 열(Column)을 읽을지 입력받음
    col_name = st.sidebar.text_input("데이터가 있는 컬럼명", value="review")
    if uploaded_file:
        # 업로드된 파일을 읽어서 corpus 주머니에 담음
        corpus = ta.load_corpus(uploaded_file, col_name)

else:
    # 긁어올 웹사이트 주소를 입력받는 창 생성
    url = st.sidebar.text_input("긁어올 웹 페이지 주소(URL) 입력")
    if url:
        # 뷰티풀스프로 웹 페이지 텍스트 추출
        res = requests.get(url)                         # 1. 해당 주소의 웹사이트에 접속 요청
        soup = BeautifulSoup(res.text, 'html.parser')   # 2. 받아온 HTML 코드를 BeautifulSoup으로 분석 준비
        # 페이지 내 모든 텍스트를 가져와서 리스트에 담기
        corpus = [soup.get_text()]                      # 3. HTML 태그는 빼고 '진짜 글자'만 추출해서 corpus 주머니에 담음

# --- 시각화 설정 영역 ---
st.sidebar.header("설정")
show_bar = st.sidebar.checkbox("빈도수 그래프", value=True)     # 그래프 보여줄지 체크박스
num_bar = st.sidebar.slider("그래프 단어 수", 10, 50, 20)       # 그래프에 띄울 단어 개수 조절
show_wc = st.sidebar.checkbox("워드클라우드", value=False)      # 워드클라우드 보여줄지 체크박스
num_wc = st.sidebar.slider("워드클라우드 단어 수", 20, 500, 50)  # 워드클라우드 단어 개수 조절
run_button = st.sidebar.button("분석 시작")                     # 클릭 시 모든 코드를 실행시키는 버튼

# --- 메인 화면 영역: 결과가 출력되는 곳 ---
st.title("텍스트 마이닝 대시보드")          # 메인 제목 출력

# 데이터가 주머니(corpus)에 있고, 사용자가 '분석 시작' 버튼을 눌렀을 때만 실행
if len(corpus) > 0 and run_button:
    # 빈도수 계산 및 시각화
    # 1. 한글 분석 선생님(Okt)을 준비함
    # 2. 명사, 동사, 형용사만 골라내고 불용어(은, 는, 이, 가 등)를 제거하여 개수를 셈
    my_tags = ['Noun', 'Verb', 'Adjective']
    my_stopwords = ['은', '는', '이', '가', '을', '를', '의', '에']
    counter = ta.count_word_freq(corpus, Okt().pos, my_tags, my_stopwords)
    
    st.success("분석이 완료되었습니다!")        # 초록색 성공 메시지 출력
    
    # 체크박스가 켜져 있다면 가로 막대 그래프를 그림
    if show_bar:
        st.subheader(f"단어 빈도수 TOP {num_bar}")
        sv.visualize_barh_graph(counter, num_bar)

    # 체크박스가 켜져 있다면 워드클라우드를 그림
    if show_wc:
        st.subheader("워드클라우드")
        sv.visualize_wordcloud(counter, num_wc)
else:
    # 아직 아무것도 안 했을 때 보여주는 안내 메시지
    st.info("데이터 소스를 선택하고 '분석 시작'을 눌러주세요.")