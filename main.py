from news import buscar_noticias
from summarizer import resumir_noticia

noticias = buscar_noticias()

for noticia in noticias[:5]:
    print("Exibindo noticia:")
    print(resumir_noticia(noticia))
