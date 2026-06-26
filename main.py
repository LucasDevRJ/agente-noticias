from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from news import buscar_noticias


parser = StrOutputParser()
noticias = buscar_noticias()
primeira_noticia = noticias[0]

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

# Executa
resposta = chain.invoke(
    {
        "titulo": primeira_noticia.title,
        "conteudo": primeira_noticia.summary
    }
)

# Mostra a resposta
print(resposta)
