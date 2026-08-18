import asyncio
from parsers.limes_parser import LimesParser

async def main():
    parser = LimesParser()
    result = await parser.parse("https://www.limesonline.com/dossier/anniversari-geopolitici-limesnerd/shakespeare-assedio-di-santo-domingo-el-cin-gli-anniversari-geopolitici-del-23-aprile-14717558/")

    print("URL:", result["url"])
    print("DOMAIN:", result["domain"])
    print("TITLE:", result["title"])
    print("\n--- PARSED TEXT (primi 1500 caratteri) ---\n")
    print(result["parsed_text"][:1500])

asyncio.run(main())