import re
from .base_parser import Parser


class LimesParser(Parser):
    """
    Parser specifico per limesonline.com
    """

    domain = "limesonline.com"

    def clean_text(self, raw_markdown: str) -> str:
        text = raw_markdown

        match = re.search(r'©\d{4} GEDI Periodici e Servizi S\.p\.A\..*?\n', text)
        if match:
            text = text[match.end():]

        text = re.sub(r'\[\s*\]\(https://(www\.)?(facebook|twitter|linkedin|web\.whatsapp)\.com[^\)]*\)', '', text)
        text = re.sub(r'!\[.*', '', text)

        # Rimuove la riga della barra di ricerca del sito
        text = re.sub(r'Scrivi qui una nuova parola\(e\) da cercare\n', '', text)
        text = re.sub(r'^\s*Cerca\s*\n', '', text, flags=re.MULTILINE)
        
        # Rimuove righe che contengono solo un puntino elenco vuoto (es. "  *")
        text = re.sub(r'^\s*\*\s*\n', '', text, flags=re.MULTILINE)

        text = re.sub(r'\n{3,}', '\n\n', text)

        return text.strip()