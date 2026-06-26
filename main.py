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