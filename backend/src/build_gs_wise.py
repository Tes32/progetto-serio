import asyncio
import json
from parsers.wise_parser import WiseParser  # verifica che il nome della classe/file corrisponda al tuo

URLS = [
    "https://wise.com/it/blog/wise-e-sicuro",
    "https://wise.com/it/blog/comprare-da-amazon-usa",
    "https://wise.com/it/blog/upwork-italia-come-funziona",
    "https://wise.com/it/blog/discriminazione-iban",
    "https://wise.com/it/blog/cro-bonifico-bancario-dove-trovarlo",
    "https://wise.com/it/blog/bonifico-sepa-cos-e-tempi",
    "https://wise.com/it/blog/rete-swift-come-funziona",
    "https://wise.com/it/blog/national-insurance-number-come-funziona",
    "https://wise.com/it/blog/cosa-serve-per-aprire-conto-corrente",
    "https://wise.com/it/blog/chiudere-conto-corrente-come-si-fa",
]


async def main():
    parser = WiseParser()
    gs_entries = []

    for url in URLS:
        print(f"Scaricando: {url}")
        result = await parser.parse(url)

        entry = {
            "url": result["url"],
            "domain": result["domain"],
            "title": result["title"],
            "html_text": result["html_text"],
            "gold_text": "" 
        }
        gs_entries.append(entry)

    output_path = "../../gs_data/wise.com_gs.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gs_entries, f, ensure_ascii=False, indent=2)

    print(f"\nFatto! Salvato in {output_path}")
    print(f"Ora apri il file e riempi il campo 'gold_text' per ciascuna delle {len(gs_entries)} voci.")


asyncio.run(main())