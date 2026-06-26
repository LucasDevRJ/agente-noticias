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
prompt = ChatPromptTemplate.from_template(
    """
    Explique o seguinte assunto como se eu tivesse 10 anos:

    {assunto}
    """
)

# Cria a Chain
chain = prompt | llm | parser

# Executa
resposta = chain.invoke(
    {
        "assunto": "Agentes de IA"
    }
)

# Mostra a resposta
print(resposta)

# Importa função
from news import buscar_noticias

# Cria variável
noticias = buscar_noticias()

# Exibe valor da variável
print(noticias)

# Especifica o tipo da variável
print(type(noticias))

# Exibe o tamanho da variável
print(len(noticias))

# Exibe a primeira notícia do vetor Noticias
print(noticias[0])

# Exibe o título da Notícia
print(noticias[0].title)

# Exibe a URL
print(noticias[0].link)

# Data da publicação
print(noticias[0].published)

# Sumario da notícia
print(noticias[0].summary)

# Exibe títulos das notícias
for noticia in noticias:
    print(noticia.title)
