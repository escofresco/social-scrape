import bs4
from extract_social_media import find_links_tree
from html_to_etree import parse_html_bytes
import requests
# res = requests.get('http://vsolvit.com/')
# tree = parse_html_bytes(res.content, res.headers.get('content-type'))
#
# print(set(find_links_tree(tree)))

def find_social_links(url) -> set:
    """
    Find the social media links are a webpage.
    - url: The url of the webpage to search (String)
    """
    response = requests.get(url)
    tree = parse_html_bytes(response.content, response.headers.get('content-type'))
    return set(find_links_tree(tree))

print(find_social_links("http://vsolvit.com/"))
