import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

MAX_TOKENS = 600
MAX_HISTORY_MESSAGES = 12

st.set_page_config(page_title="AskCV — Onkar Dureja", page_icon="💬")


@st.cache_resource
def get_client():
    return Groq(api_key=GROQ_API_KEY)


@st.cache_data
def load_portfolio_data():
    with open("portfolio_data.md", "r", encoding="utf-8") as f:
        return f.read()


def build_system_prompt():
    portfolio_data = load_portfolio_data()
    return f"""You are AskCV, a conversational assistant that answers recruiter questions about Onkar Dureja based strictly on the portfolio data below.

Hard rule: only answer using information present in the portfolio data. If something is not covered there, say plainly that this isn't part of Onkar's current portfolio data. Never guess, estimate, or infer skills, experience, or numbers that are not explicitly stated.

Keep answers concise and professional. You are speaking to recruiters and hiring managers.

--- PORTFOLIO DATA START ---
{portfolio_data}
--- PORTFOLIO DATA END ---
"""


client = get_client()

st.title("AskCV")
st.caption("Ask me anything about Onkar's background, skills, and projects.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask about Onkar's experience, skills, or projects...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    history = st.session_state.messages[-MAX_HISTORY_MESSAGES:]
    api_messages = [{"role": "system", "content": build_system_prompt()}] + history

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        try:
            stream = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=api_messages,
                max_tokens=MAX_TOKENS,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    full_response += delta
                    placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Something went wrong talking to the model: {e}"
            placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})