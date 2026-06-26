from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# Carrega o .env
load_dotenv()

# Modelo
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
    Você é um jornalista.

    Faça um resumo da notícia abaixo em no máximo 3 frases.

    Título:
    {titulo}

    Conteúdo:
    {conteudo}
""")

# Cria a Chain
chain = prompt | llm | parser

def resumir_noticia(noticia): 
    resposta = chain.invoke(
        {
            "titulo": noticia.title,
            "conteudo": noticia.summary
        }
    )
    return resposta
