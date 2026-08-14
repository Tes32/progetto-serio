import asyncio
import json
from parsers.limes_parser import LimesParser  

URLS = [
    "https://www.limesonline.com/rubriche/fiamme-americane/trump-politica-estera-sovranismo-america-first-interessi-nazionali-usa-22450527/?ref=LHTP-BH-I22530847-P2-S2-T1",
    "https://www.limesonline.com/rubriche/fiamme-americane/cuba-america-donald-trump-marco-rubio-raul-castro-venezuela-22527309/?ref=LHTP-BH-I22530847-P2-S1-T1",
    "https://www.limesonline.com/articoli/trieste-torna-contesa-22520036/?ref=LHTP-BH-I21635809-P3-S1-T1",
    "https://www.limesonline.com/articoli/francesco-guccini-geopolitica-conflitto-canzoni-italia-22499739/?ref=LHTP-BH-I21635809-P3-S2-T1",
    "https://www.limesonline.com/rubriche/il-punto/ceuta-immigrazione-migranti-spagna-marocco-schengen-giorgia-meloni-italia-demografia-integrazione-lucio-caracciolo-22478183/?ref=LHTP-BH-I21635809-P3-S3-T1", #
    "https://www.limesonline.com/articoli/piano-padre-come-riformare-debito-europa-sovranita-stati-22518952/?ref=LHTP-BH-I21874390-P6-S1-T1",
    "https://www.limesonline.com/dossier/strillone-beirut-rassegna-mediorientale/il-prezzo-variabile-della-sicurezza-dell-arabia-saudita-golfo-hormuz-petrolio-nucleare-usa-iran-eau-yemen-22489288/?ref=LHTP-BH-I22069694-P7-S1-T1",
    "https://www.limesonline.com/rivista/il-senso-delle-petromonarchie-per-l-iran-22451281/",
    "https://www.limesonline.com/rivista/editoriale-del-numero-di-limes-726--gli-stretti-indispensabili--22456335/",
    "https://www.limesonline.com/articoli/rapporti-russia-con-turchia-e-israele-22016783/"

]


async def main():
    parser = LimesParser()
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

    output_path = "../../gs_data/limesonline.com_gs.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gs_entries, f, ensure_ascii=False, indent=2)

    print(f"\nFatto! Salvato in {output_path}")


asyncio.run(main())
