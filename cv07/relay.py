#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ukázka pár triků jak urychlit program
"""
import codecs
import inspect
import json
import re
HTML_RESULT = 'result.html'
JSON_COMPETITORS = 'competitors.json'


def name_hook(obj, dct={}):
    """
    mutable typ jako defaultni hodnota může být nebezpečnej.
    pylint říká:
    Dangerous default value {} as argument
    Je to dirty trick ale občas se toho využívá.
    """
    dct.update({obj["firstname"] + ' ' + obj["lastname"]: obj["id"]})


class FixJson(object):  # pylint: disable=too-few-public-methods
    """
    opravi escapnutej apostrof v souboru (pokud jste tak neučinili)
    a to bez nutnosti cist celej soubor
    """
    def __init__(self, file):
        self.jfile = file

    def read(self):
        """
        wrapper pro read(), nic víc.
        """
        fread = self.jfile.read()
        print(fread)
        return re.sub(r'\\\'', '\'', fread)


def relay():
    """
    extract data from html and json and concatenate them into new json file
    :return: json with result
    """
    # Load data from html, BS4 by se tu hodil
    with codecs.open(HTML_RESULT, 'r', encoding='utf-8') as html_file:
        records = []
        while 1:
            if html_file.__next__().strip() == '<p><strong>Relay</strong></p>':
                for _ in range(4):
                    records += re.findall(
                        r'(\d+)\) .+?(\d{0,2}:\d{0,2}:\d{0,2}) \(([\w ,]*)\)'
                        , html_file.__next__().strip())
                break

    # Load data from json
    with codecs.open(JSON_COMPETITORS, 'r', encoding='utf-8') as json_file:
        json.load(FixJson(json_file), object_hook=name_hook)
    data = inspect.signature(name_hook).parameters['dct'].default
    # pylint je otravnej disable=name_hook.__defaults__[0]
    # data = name_hook.__defaults__[0]

    # parse to JSON
    return json.dumps(
        [{"result": int(rec[0]), "time": rec[1], "id": int(data[name])}
         for rec in records
         for name in rec[2].split(', ')
         if name in data]
        , sort_keys=True
        , indent=4
    )


if __name__ == '__main__':
    print(relay())
