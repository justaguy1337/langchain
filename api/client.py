import requests
import streamlit as st

def extract_text(output):
    content = output.get('content', output) if isinstance(output, dict) else output
    if isinstance(content, list):
        return "".join(part.get("text", "") if isinstance(part, dict) else str(part) for part in content)
    return str(content)

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input':{'topic':input_text}})
    return extract_text(response.json()['output'])


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic':input_text}})
    return extract_text(response.json()['output'])

st.title('Langchain Demo With Gemini/Ollama API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

