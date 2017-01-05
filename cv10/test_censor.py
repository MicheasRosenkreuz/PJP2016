# -*- coding: utf-8 -*-

"""
Py.test testy pro censor module

Pokud máte nainstalovaný program PyTest stačí ho spustit v adresáři s testem
příkazem py.test

PyTest si sám najde testy a postará se o jejich provedení.

PyTest si můžete nainstalovat přes pip a je také součástí distribuce Anaconda
"""

import codecs

import censor

FINPUT = "test_input.html"
FLIST = "test_list.txt"
FOUTPUT = "test_output.txt"
FOUTPUT1 = "test_output1.txt"

def test_cleanbannedwords():
    """
    Test clen banned words
    """
    with codecs.open(FINPUT, 'r') as fil:
        textin = fil.read()
    with codecs.open(FOUTPUT, 'r') as fil:
        textout = fil.read()
    assert censor.clean_banned_words(FLIST, textin) == textout

def test_cleantags():
    """
    Test clean tags
    """
    with codecs.open(FOUTPUT1, 'r', encoding='utf8') as fil:
        textout = fil.read()
    assert censor.clean_tags(FINPUT) == textout

def test_argumentparser():
    '''
    Test argument parser
    '''
    parser = censor.argument_parser(['-i a', '-l b', '-c'])
    assert parser == (' a', ' b', False)
