from bs4 import BeautifulSoup
from extract_social_media import find_links_tree
import getopt
from html_to_etree import parse_html_bytes
import queue
import requests
import sys


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
        if link['href'].startswith('/') or link['href'].startswith('\\'):
            links.add(link['href'])
    return links

def bfs(url) -> set:
    queue = []
    queue.append(url)
    queue[url] = True
    while queue:
        social_links = find_social_links(url)
        if (len(social_links) > 0):
            return social_links
        else:
            response = requests.get(url)
            links = page_links(response)

def main(argv):
    url = ''
    try:
        opts, args = getopt.getopt(argv, 'hu:', ['help', 'url='])
    except getopt.GetoptError:
        print('social_scrape.py -u <url>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('social_scrape.py -u <url>')
            sys.exit()
        elif opt in ('-u', '--url'):
            url = arg
    print('Url is '+url)

if __name__ == "__main__":
    main(sys.argv[1:])
