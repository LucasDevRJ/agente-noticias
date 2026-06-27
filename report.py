def gerar_relatorio(resumos):
    relatorio = "Relatório de Notícias:\n\n"

    for resumo in resumos:
        relatorio += f"Título: {resumo['titulo']}\n"
        relatorio += f"Resumo: {resumo['resumo']}\n"
        relatorio += f"Link: {resumo['link']}\n"
        relatorio += "-" * 40 + "\n"

    return relatorio