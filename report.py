def gerar_relatorio(resumos):
    """
    Gera um relatório em formato de texto a partir de uma lista de resumos de notícias.

    Args:
        resumos (list): Lista de dicionários contendo os resumos das notícias.

    Returns:
        str: Relatório em formato de texto.
    """
    relatorio = "Relatório de Notícias:\n\n"
    for resumo in resumos:
        relatorio += f"Título: {resumo['titulo']}\n"
        relatorio += f"Resumo: {resumo['resumo']}\n"
        relatorio += f"Link: {resumo['link']}\n"
        relatorio += "-" * 40 + "\n"
    return relatorio