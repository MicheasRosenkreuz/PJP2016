# -*- coding: utf-8 -*-
"""
@author: Jiri Vrany
@author: Frantisek Jukl
@author: Michal Jirasek

Pro použití je potřeba balíček py.test.
Instaluje se přes pip příkazem pip install pytest.

Zbytek je snadný, nakopírujte tento soubor do adresáře s
řešením a z příkazové řádky
spusťe test - příkazem py.test

Pytest prohledá aktuální adresář (a adresáře vnořené) a spustí
nalezené testy.

"""
import cestina


def test_nothing():
    """
    testovani niceho
    """
    text = ""
    result = []
    assert result == cestina.split_text(text)


def test_insane():
    """
    testovani insane
    """
    text = (u'To tedy  byl opravdu "úspěch". Fucking Frydek-Mistek. '
            'Např.: "A to všechno," povídá Jarmila nahlas, "je mou vinou." '
            'Hory a oceán -- to jsou dva živly, jichž je plna jeho poezie;')
    result = ['To',
              'tedy',
              'byl',
              'opravdu',
              'úspěch',
              'Fucking',
              'Frydek-Mistek',
              'Např',
              'A',
              'to',
              'všechno',
              'povídá',
              'Jarmila',
              'nahlas',
              'je',
              'mou',
              'vinou',
              'Hory',
              'a',
              'oceán',
              'to',
              'jsou',
              'dva',
              'živly',
              'jichž',
              'je',
              'plna',
              'jeho',
              'poezie']
    assert result == cestina.split_text(text)


def test_pred_a_po():
    """
    testovani pred a po slove
    """
    text = (u'"Co by to bylo, kdyby to byla láska" je kniha od J. Kostrhuna, '
            '"Dívka, na které nezáleželo" od P. Francouze. -- Vyslechli jsme '
            'symfonii "S úderem kotlů" od J. Haydna;')
    result = ['Co',
              'by',
              'to',
              'bylo',
              'kdyby',
              'to',
              'byla',
              'láska',
              'je',
              'kniha',
              'od',
              'J',
              'Kostrhuna',
              'Dívka',
              'na',
              'které',
              'nezáleželo',
              'od',
              'P',
              'Francouze',
              'Vyslechli',
              'jsme',
              'symfonii',
              'S',
              'úderem',
              'kotlů',
              'od',
              'J',
              'Haydna']
    assert result == cestina.split_text(text)


def test_cesky():
    """
    jenoduchy test kodovani cestiny
    """
    text = u'šíleně žluťoučký kůň'
    result = ['šíleně', 'žluťoučký', 'kůň']
    assert cestina.split_text(text) == result


def test_split_text():
    """
    test pro kratky text
    """
    text = (u'Programovací jazyk Python přispívá k '
            'rychlému vývoji. Python se sice snaží být intuitivní, '
            'ale obsahuje věci, které nejsou všední, a příliš se o nich neví. '
            '\n '
            'A nyní něco úplně jiného: jedna. Kde leží Frýdek-Místek? '
            'Jedna + jedna se rovná? Totéž co čtyři / dvěma!')

    result = [
        'Programovací',
        'jazyk',
        'Python',
        'přispívá',
        'k',
        'rychlému',
        'vývoji',
        'Python',
        'se',
        'sice',
        'snaží',
        'být',
        'intuitivní',
        'ale',
        'obsahuje',
        'věci',
        'které',
        'nejsou',
        'všední',
        'a',
        'příliš',
        'se',
        'o',
        'nich',
        'neví',
        'A',
        'nyní',
        'něco',
        'úplně',
        'jiného',
        'jedna',
        'Kde',
        'leží',
        'Frýdek-Místek',
        'Jedna',
        'jedna',
        'se',
        'rovná',
        'Totéž',
        'co',
        'čtyři',
        'dvěma']

    assert result == cestina.split_text(text)


def test_cesky2():
    """
    test
    """
    text = ('Letos je tomu 41 let. Ten říjnový den jsem utíkala z budovy '
            'konzervatoře do knihovny na Mariánském náměstí, abych se '
            '„zakousla“ do regálu nadepsaného Poezie. Abych poprvé listovala '
            'knížkou Pootevřený anděl v šedé obálce, a později objevila další '
            'knížku Karla Sýse Dlouhé sbohem v tmavě zelené obálce, a také '
            'obálku světle zelenou – Florianovu Jízdu na luční kobylce…')

    result = ['Letos',
              'je',
              'tomu',
              '41',
              'let',
              'Ten',
              'říjnový',
              'den',
              'jsem',
              'utíkala',
              'z',
              'budovy',
              'konzervatoře',
              'do',
              'knihovny',
              'na',
              'Mariánském',
              'náměstí',
              'abych',
              'se',
              'zakousla',
              'do',
              'regálu',
              'nadepsaného',
              'Poezie',
              'Abych',
              'poprvé',
              'listovala',
              'knížkou',
              'Pootevřený',
              'anděl',
              'v',
              'šedé',
              'obálce',
              'a',
              'později',
              'objevila',
              'další',
              'knížku',
              'Karla',
              'Sýse',
              'Dlouhé',
              'sbohem',
              'v',
              'tmavě',
              'zelené',
              'obálce',
              'a',
              'také',
              'obálku',
              'světle',
              'zelenou',
              'Florianovu',
              'Jízdu',
              'na',
              'luční',
              'kobylce']

    assert result == cestina.split_text(text)
