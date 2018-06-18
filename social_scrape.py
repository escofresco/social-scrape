import bs4 import BeautifulSoup
from extract_social_media import find_links_tree
from html_to_etree import parse_html_bytes
import requests

def find_social_links(url) -> set:
    """
    Find the social media links are a webpage.
    - url: The url of the webpage to search (String)
    """
    response = requests.get(url)
    tree = parse_html_bytes(response.content, response.headers.get('content-type'))
    return set(find_links_tree(tree))

#print(find_social_links("http://vsolvit.com/"))
def page_links(html_cnt) -> set:
    soup = BeautifulSoup(html_cnt, 'lxml')
    links = set()
    for link in set(soup.find_all('a')):
        if link['href'].startswith('/') or link['href'].startswith('\'):
            links.add(link['href'])
    return links

def bfs(url) -> set :
    social_links = find_social_links(url)
    if (len(social_links) > 0):
        return social_links
    else:
        response = requests.get(url)
        links

if __name__ == "__main__":
