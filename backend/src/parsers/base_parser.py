from abc import ABC, abstractmethod
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig


class Parser(ABC):
    domain: str = ""

    def get_config(self) -> CrawlerRunConfig:
        return CrawlerRunConfig(
            excluded_tags=['nav', 'header', 'footer', 'aside'],
            word_count_threshold=10
        )

    async def download(self, url: str):
        config = self.get_config()
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url, config=config)
        return result

    @abstractmethod
    def clean_text(self, raw_markdown: str) -> str:
        pass

    async def parse(self, url: str) -> dict:
        result = await self.download(url)
        parsed_text = self.clean_text(result.markdown)

        return {
            "url": url,
            "domain": self.domain,
            "title": result.metadata.get("title", "").replace(" - Wikipedia", "").replace(" - Wise", "").replace(" - People", "").replace(" - Limes", ""),
            "html_text": result.html,
            "parsed_text": parsed_text
        }