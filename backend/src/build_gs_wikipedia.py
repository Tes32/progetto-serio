import asyncio
import json
from parsers.wiki_parser import WikipediaParser

URLS = [
    "https://it.wikipedia.org/wiki/Galassia_di_Andromeda", #FATTO
    "https://it.wikipedia.org/wiki/Lago_di_Lugano", #FATTO
    "https://it.wikipedia.org/wiki/Sistema_stellare", 
    "https://it.wikipedia.org/wiki/Fiera_Colombiana_di_Chicago", #CORRETTO
    "https://it.wikipedia.org/wiki/Golfo_di_Gaeta", #CORRETTO
    "https://it.wikipedia.org/wiki/Singolarit%C3%A0_gravitazionale", #CORRETTO
    "https://it.wikipedia.org/wiki/Penombra",  #CORRETTO
    "https://it.wikipedia.org/wiki/Theia_(pianeta_ipotetico)", 
    "https://it.wikipedia.org/wiki/Galassia_ellittica", 
    "https://it.wikipedia.org/wiki/Parco_nazionale"   #CORETTO
]


async def main():
    parser = WikipediaParser()
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

    # Salva tutto in un file JSON dentro gs_data/
    output_path = "../../gs_data/it.wikipedia.org_gs.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gs_entries, f, ensure_ascii=False, indent=2)

    print(f"\nFatto! Salvato in {output_path}")
    print(f"Ora apri il file e riempi il campo 'gold_text' per ciascuna delle {len(gs_entries)} voci.")


asyncio.run(main())