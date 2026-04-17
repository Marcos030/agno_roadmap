import requests
import streamlit as st

API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Team Analista", page_icon="📊", layout="centered")
st.title("📊 Team Analista")
st.caption("Converse com o time de agentes de análise financeira.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = "streamlit_session"
if "user_id" not in st.session_state:
    st.session_state.user_id = "streamlit_user"

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analisando..."):
            response = requests.post(
                API_URL,
                json={
                    "message": prompt,
                    "session_id": st.session_state.session_id,
                    "user_id": st.session_state.user_id,
                },
                timeout=300,
            )
            response.raise_for_status()
            answer = response.json()["response"]
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

#Para rodar:
## 1. Subir a API primeiro:  uv run python hello_agno_streamlite.py
## 2. Subir a UI:            uv run streamlit run hello_agno_streamlit_UI.py
