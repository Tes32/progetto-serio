import re

from .base_parser import Parser


class WikipediaParser(Parser):
    """
    Parser specifico per it.wikipedia.org.

    Eredita da Parser tutta la logica comune (download, parse)
    e implementa solo clean_text, specifico per Wikipedia.
    """

    domain = "it.wikipedia.org"

    def clean_text(self, raw_markdown: str) -> str:
        text = raw_markdown

        # Rimuove "Vai al contenuto"
        text = re.sub(r'\[Vai al contenuto\].*?\n', '', text)

        # Rimuove box di disambiguazione
        text = re.sub(r'\[Disambiguazione\].*?\n', '', text)

        # Rimuove immagini Markdown
        text = re.sub(r'!\[.*', '', text)

        # Rimuove i link "modifica / modifica wikitesto"
        text = re.sub(
            r'\[\[modifica\].*?\]',
            '',
            text
        )

        # Elimina tutto da "Note" in poi
        text = re.split(r'\n## Note\s*\n', text, maxsplit=1)[0]

        # Rimuove righe vuote multiple
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text.strip()