from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega o .env
load_dotenv()

# Modelo
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Parser
parser = StrOutputParser()

# Prompt
prompt = ChatPromptTemplate.from_template("""
Você é um jornalista.

Faça um resumo da notícia abaixo em no máximo 3 frases.

Título:
{titulo}

Conteúdo:
{conteudo}
""")

# Chain
chain = prompt | llm | parser


def resumir_noticia(noticia):
    return chain.invoke(
        {
            "titulo": noticia.title,
            "conteudo": noticia.summary
        }
    )