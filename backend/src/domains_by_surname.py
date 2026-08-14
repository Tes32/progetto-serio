import hashlib

# Numero totale di domini disponibili per l'assegnazione.
# Verrà usato anche dal docente per verificare la correttezza dell'assegnazione, quindi non modificarlo.
DOMINI = 148
# Lettere "dispari" (A, C, E, ..., Y) -> Wikipedia in inglese, altrimenti italiano
LETTERE_DISPARI = set("ACEGIKMOQSUWY")

def wikipedia_lingua(cognomi: list[str]) -> str:
    """Ritorna 'en' o 'it' in base all'iniziale del primo cognome ordinato."""
    primo = sorted(c.strip().upper() for c in cognomi)[0]
    return "en" if primo[0] in LETTERE_DISPARI else "it"

def assegna_domini(cognomi: list[str]) -> list[int]:
    """Ritorna 3 numeri distinti in [1, DOMINI] derivati deterministicamente dai cognomi."""
    # 1. Normalizza (maiuscolo, no spazi), ordina e unisci con "|"
    cognomi_norm = sorted(c.strip().upper() for c in cognomi)
    chiave = "|".join(cognomi_norm)
    # 2. SHA-256: 32 byte, distribuzione uniforme, ordine-invariante
    digest = hashlib.sha256(chiave.encode("utf-8")).digest()
    # 3. Scorri la digest a finestre di 2 byte; mappa ogni coppia in [1, DOMINI]
    numeri = []
    i = 0
    while len(numeri) < 3 and i < len(digest) - 1:
        valore = int.from_bytes(digest[i:i+2], "big") % DOMINI + 1
        if valore not in numeri:
            numeri.append(valore)
        i += 1
    return numeri

def assegna_gruppo(cognomi: list[str]) -> dict:
    """Restituisce il riepilogo completo dell'assegnazione per il gruppo."""
    lingua = wikipedia_lingua(cognomi)
    return {
        "cognomi":           sorted(c.strip().upper() for c in cognomi),
        "wikipedia":         f"{lingua}.wikipedia.org",
        "domini_aggiuntivi": assegna_domini(cognomi),
    }


# Esempi di test
# print(assegna_gruppo(["Rossi"]))  # 'R' dispari? No  -> it.wikipedia.org | [71, 128, 92]
# print(assegna_gruppo(["Esposito", "Bianchi"])) # primo='BIANCHI', 'B' dispari? No  -> it.wikipedia.org | [103, 62, 126]
# print(assegna_gruppo(["Alfieri", "Esposito", "Rossi"])) # primo='ALFIERI', 'A' dispari? Sì -> en.wikipedia.org | [53, 107, 29]

# Modifica i cognomi per verificare che l'assegnazione sia stabile e invariante all'ordine 
print(assegna_gruppo(["BOCCELLA", "-", "-"])) 