from news import buscar_noticias
from summarizer import resumir_noticia

resumos = []
noticias = buscar_noticias()

for noticia in noticias[:5]:
    resumos.append(
        {
            "titulo": noticia.title,
            "resumo": resumir_noticia(noticia),
            "link": noticia.link
        }
    )
    
print(resumos)