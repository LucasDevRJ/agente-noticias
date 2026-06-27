from langchain_core.tools import tool
from news import buscar_noticias
from summarizer import resumir_noticia

@tool
def buscar_noticias_tool():
    """
    Busca as notícias mais recentes do RSS do G1.
    """
    return buscar_noticias()

@tool
def resumir_noticia_tool(titulo: str, conteudo: str):
    """
    Resume uma notícia.
    """

    class Noticia:
        def __init__(self, title, summary):
            self.title = title
            self.summary = summary

    noticia = Noticia(titulo, conteudo)

    return resumir_noticia(noticia)