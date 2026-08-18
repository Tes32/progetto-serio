import re
import mistune
from bs4 import BeautifulSoup

def remove_markdown(md: str) -> str:
    """
    Rimuove il Markdown da una stringa, restituendo solo il testo pulito.
    Usa la libreria mistune per convertire il Markdown in HTML, poi BeautifulSoup per estrarre solo il testo.
    """
    html = mistune.html(md)
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(True):
        tag.unwrap()
    text = re.sub(r'[ \t]+', ' ', str(soup))
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def token_level_eval(parsed_text: str, gold_text: str) -> dict:
    """
    Calcola precision, recall e F1 a livello di token tra il testo estratto
    dal parser (Markdown) e il Gold Standard (plain text).
    """
    # 1. Il testo del parser è in Markdown: va ripulito prima del confronto
    parsed_clean = remove_markdown(parsed_text)

    # 2. Tokenizzazione: minuscolo, split per spazio, come richiesto dalla slide
    tokens_estratti = set(parsed_clean.lower().split())
    tokens_gs = set(gold_text.lower().split())

    # 3. Intersezione tra i due insiemi di token
    intersezione = tokens_estratti & tokens_gs

    # 4. Calcolo delle metriche, gestendo i casi limite (divisione per zero)
    precision = len(intersezione) / len(tokens_estratti) if tokens_estratti else 0.0
    recall = len(intersezione) / len(tokens_gs) if tokens_gs else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4)
    }