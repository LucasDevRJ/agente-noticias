from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from tools import buscar_noticias_tool, resumir_noticia_tool

# Carrega o .env
load_dotenv()

# Modelo
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Agente
agent = create_agent(
    model=llm,
    tools=[
        buscar_noticias_tool,
        resumir_noticia_tool
    ]
)