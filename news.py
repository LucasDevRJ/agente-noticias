import feedparser

RSS_URL = "https://g1.globo.com/rss/g1/"


def buscar_noticias():
    feed = feedparser.parse(RSS_URL)

    return feed.entries