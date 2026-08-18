from .wiki_parser import WikipediaParser
from .wise_parser import WiseParser
from .people_parser import PeopleParser
from .limes_parser import LimesParser


def get_parser_for_url(url: str):
    """
    Restituisce l'istanza del parser giusto in base al dominio
    presente nell'URL. Restituisce None se il dominio non è supportato.
    """
    if "wikipedia.org" in url:
        return WikipediaParser()
    elif "wise.com" in url:
        return WiseParser()
    elif "people.com" in url:
        return PeopleParser()
    elif "limesonline.com" in url:
        return LimesParser()
    else:
        return None