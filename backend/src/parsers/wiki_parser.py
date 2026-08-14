import re
from .base_parser import Parser


class WikipediaParser(Parser):
    """
    Parser specifico per it.wikipedia.org
    Eredita da Parser tutta la logica comune (download, parse)
    e implementa solo clean_text, specifico per Wikipedia.
    """

    domain = "it.wikipedia.org"

    def clean_text(self, raw_markdown: str) -> str:
        text = raw_markdown

        # Rimuove la riga "Vai al contenuto" iniziale (link di accessibilità)
        text = re.sub(r'\[Vai al contenuto\].*?\n', '', text)

        # Rimuove i box di disambiguazione
        text = re.sub(r'\[Disambiguazione\].*?\n', '', text)

        # Rimuove le immagini in formato Markdown: ![...](...)
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)

        # Rimuove righe vuote multiple, lasciandone al massimo una
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text.strip()