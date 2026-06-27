llm = ChatOpenAI(...)

agent = create_agent(
    model=llm,
    tools=[
        buscar_noticias,
        resumir_noticia,
        gerar_relatorio
    ]
)