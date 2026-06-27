from news import buscar_noticias
from summarizer import resumir_noticia
from report import gerar_relatorio
from agent_test import soma

relatorio = ""
resumos = []
noticias = buscar_noticias()

for noticia in noticias[:5]:

    resumo = resumir_noticia(noticia)

    resumos.append(
        {
            "titulo": noticia.title,
            "resumo": resumo,
            "link": noticia.link
        }
    )

    relatorio = gerar_relatorio(resumos)


print(relatorio)