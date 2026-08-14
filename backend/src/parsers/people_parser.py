import re
from .base_parser import Parser


class PeopleParser(Parser):
    """
    Parser specifico per people.com
    """

    domain = "people.com"

    def clean_text(self, raw_markdown: str) -> str:
        text = raw_markdown

        # Rimuove intere righe che iniziano con un'immagine Markdown
        text = re.sub(r'!\[.*', '', text)

        # Rimuove il link alle linee guida editoriali
        text = re.sub(r'\[People Editorial Guidelines\]\(.*?\)', '', text)

        # Rimuove il contatore commenti
        text = re.sub(r'\[\s*\d+\s*Comments?\s*\]\(.*?\)', '', text)

        # Rimuove le righe "Credit :" delle immagini
        text = re.sub(r'Credit\s*:.*?\n', '', text)

        # Rimuove righe vuote multiple
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text.strip()