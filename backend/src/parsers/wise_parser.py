import re
from .base_parser import Parser


class WiseParser(Parser):
    """
    Parser specifico per wise.com
    """

    domain = "wise.com"

    def clean_text(self, raw_markdown: str) -> str:
        text = raw_markdown

        # Rimuove il link "Skip to main content"
        text = re.sub(r'\[Skip to main content\].*?\n', '', text)

        # Rimuove le immagini in formato Markdown
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)

        # Rimuove link "vuoti" tipo [](url), spesso decorativi/icone
        text = re.sub(r'\[\]\(.*?\)', '', text)

        # Rimuove call-to-action promozionali comuni
        text = re.sub(r'\[Sign up\]\(.*?\)', '', text)
        text = re.sub(r'\[Send money\]\(.*?\)', '', text)

        # Rimuove righe vuote multiple
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text.strip()