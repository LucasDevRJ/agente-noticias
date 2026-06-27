from agent import agent

resposta = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Busque as últimas notícias."
            }
        ]
    }
)

ultima_resposta = resposta["messages"][-1]

print(ultima_resposta.content)