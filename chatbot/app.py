from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the queries"),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.title("Langchain demo with Gemini API")
input_text = st.text_input("Search the topic you want")

#OpenAI LLM
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))