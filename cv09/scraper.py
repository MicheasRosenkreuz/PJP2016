#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from pprint import pprint
from urllib.request import Request, urlopen, HTTPError
from urllib.parse import urlparse, urljoin, urlencode
from html.parser import HTMLParser

__author__ = "Michal Jirásek"
__email__ = "michal.jirasek@tul.cz"
#__credits__ = []

class HREFParser(HTMLParser):
    """
    Parser that extracts hrefs
    """
    def __init__(self):
        super().__init__()
        self.hrefs = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                self.hrefs.add(dict_attrs['href'])




class Crawler(object):
    def __init__(self):
        self.tree = {}  # defaultdict(list)
        self.fetched_mails = set()

    def crawl(self, url):
        # self._root = '/'.join(url.split('/')[:-1]) + '/'
        self._root = urlparse(url).path
        self._crawl([url,])

    def _visited(self, url):
        path = urlparse(url).path.split('/')
        if 'index.' in path[-1]:  # pokud se soubor jmenuje index nezávisle na příponě
            return urljoin(url, '/'.join(path[:-1]) + '/') not in self.tree
        else:
            return url not in self.tree

    def _crawl(self, urls):
        for url in urls:
            u_parse = urlparse(url)
            if self._visited(url):
                self.tree[url] = []  # bez pouzití defaultdict
                # bcaus it cen be a good evidence of visited urls

                html = self._request(url)
                self.fetched_mails.union(self._crawl_emails(html))
                fetched_urls = self._crawl_urls(html, url, u_parse.netloc)
                # print('_crawling: ', url, fetched_u)
                self._populate_tree(url, fetched_urls)
                self._crawl(fetched_urls)

    def _populate_tree(self, base, childern):
        for ch in childern:
            self.tree[base].append(ch)

    def _crawl_urls(self, html, base, domain):
        hrefs = set()
        parser = HREFParser()
        parser.feed(html)
        for href in parser.hrefs:
            u_parse = urlparse(href)
            if href.startswith('/'):
                # purposefully using path, no query, no hash
                hrefs.add(u_parse.path)
            else:
                # only keep the local urls
                if u_parse.scheme in ('', 'http', 'https') \
                        and u_parse.netloc in (domain, ''):
                    hrefs.add(urljoin(base, u_parse.path))
        return hrefs

    def _crawl_emails(self, html):
        return {}

    def _request(self, url):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            print("retrieving url... [%s] " % url)
            req = Request(url)
            response = urlopen(req)
            return response.read().decode('ascii', 'ignore')
        except HTTPError as e:
            print("error [%s] : %s" % (url, e))
        return ''


if __name__ == "__main__":
    crawler = Crawler()
    # crawler.crawl('http://www.nti.tul.cz/~vrany/pjp_data/')
    crawler.crawl('http://www.fr.4fan.cz/pjp/index.html')
    print(crawler._root)
    pprint(crawler.tree)

