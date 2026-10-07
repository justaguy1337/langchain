from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes  
import uvicorn
import os
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

app = FastAPI(
    title="LangChain Server", 
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-3.8-flash"),
    path="/openai",
)

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
##ollama llama2
llm = ChatOllama(model="llama3.1")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 year child with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)
