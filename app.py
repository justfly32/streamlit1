import streamlit as st
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# OpenAI API 키 설정
openai_api_key = '

# 대화형 GPT 모델 설정 (OpenAI API 사용)
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# 대화 기억을 위한 메모리 설정
memory = ConversationBufferMemory(return_messages=True)

# ConversationChain을 사용하여 대화 흐름 관리
conversation_chain = ConversationChain(llm=llm, memory=memory)

# Streamlit 웹 페이지 제목 설정
st.title("LangChain 기반 GPT 챗봇")

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:", "")

# 사용자 질문이 있을 때 GPT 모델로 처리
if user_input:
    with st.spinner("GPT가 답변을 생성하고 있습니다..."):
        response = conversation_chain.run(input=user_input)
        st.write("**챗봇 응답:**")
        st.write(response)

# 대화 기록 출력
st.header("대화 기록")
st.write(memory.buffer)
