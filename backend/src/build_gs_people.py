import asyncio
import json
from parsers.people_parser import PeopleParser  # verifica nome classe/file

URLS = [
    "https://people.com/whitney-leavitt-is-returning-to-broadway-to-star-in-just-in-time-exclusive-12057592",
    "https://people.com/moulin-rouge-kelsie-watts-fight-nearly-broke-out-in-audience-12057807",
    "https://people.com/human-remains-found-in-state-park-nearly-50-years-ago-identified-as-missing-canadian-man-12058253",
    "https://people.com/hoku-left-pop-stardom-record-label-ultimatum-eyeing-return-exclusive-12037733",
    "https://people.com/jennifer-nettles-kristian-bush-secret-to-sugarland-success-12057622",
    "https://people.com/starbucks-unicorn-frappuccino-returns-this-weekend-and-we-got-an-early-taste-12058919",
    "https://people.com/unauthorized-wi-fi-network-pops-up-during-delta-flight-prompting-investigation-12058586",
    "https://people.com/nicole-kidman-makes-rare-comments-about-completely-natural-marriage-to-tom-cruise-12058852",
    "https://people.com/demi-lovato-reveals-biggest-takeaway-from-her-first-year-of-marriage-exclusive-12056882",
    "https://people.com/mike-chen-of-sorcery-and-science-excerpt-exclusive-12058538"
]


async def main():
    parser = PeopleParser()
    gs_entries = []

    for url in URLS:
        print(f"Scaricando: {url}")
        result = await parser.parse(url)

        entry = {
            "url": result["url"],
            "domain": result["domain"],
            "title": result["title"],
            "html_text": result["html_text"],
            "gold_text": ""  # <-- lo scrivi TU a mano
        }
        gs_entries.append(entry)

    output_path = "../../gs_data/people.com_gs.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(gs_entries, f, ensure_ascii=False, indent=2)

    print(f"\nFatto! Salvato in {output_path}")


asyncio.run(main())
