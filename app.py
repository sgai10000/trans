import streamlit as st
from deep_translator import GoogleTranslator

# 웹페이지 기본 설정
st.set_page_config(page_title="다국어 번역기", page_icon="🌐", layout="centered")

# 화면 제목
st.title("🌐 한국어 다국어 번역기")
st.write("한국어를 입력하면 영어, 일본어, 중국어, 프랑스어로 동시 번역해 줍니다.")

# 텍스트 입력 창
text_to_translate = st.text_area("번역할 한국어 입력", placeholder="여기에 한국어로 문장을 입력하세요.")

# 번역 버튼
if st.button("번역하기", type="primary"):
    if text_to_translate.strip():
        # 로딩 스피너 표시
        with st.spinner("번역을 진행하고 있습니다..."):
            try:
                # deep-translator를 사용한 다국어 번역 수행
                en = GoogleTranslator(source='ko', target='en').translate(text_to_translate)
                ja = GoogleTranslator(source='ko', target='ja').translate(text_to_translate)
                zh = GoogleTranslator(source='ko', target='zh-CN').translate(text_to_translate) # 중국어 간체
                fr = GoogleTranslator(source='ko', target='fr').translate(text_to_translate)

                st.success("번역이 완료되었습니다!")
                
                # 결과 출력 (2단 컬럼 레이아웃)
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("🇺🇸 영어")
                    st.info(en)
                    st.subheader("🇨🇳 중국어")
                    st.info(zh)
                    
                with col2:
                    st.subheader("🇯🇵 일본어")
                    st.info(ja)
                    st.subheader("🇫🇷 프랑스어")
                    st.info(fr)
                    
            except Exception as e:
                st.error(f"번역 중 오류가 발생했습니다: {e}")
    else:
        st.warning("번역할 텍스트를 먼저 입력해주세요.")
