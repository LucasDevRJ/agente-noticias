from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from agent_test import soma

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

agent = create_agent(
    model=llm,
    tools=[soma]
)

resposta = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Quanto é 15 + 37?"
            }
        ]
    }
)

print(resposta)