# -*- coding: utf-8 -*-
"""
Motivace: dveře jsou uzavřeny speciálním druhem zámku, který se otevírá vyřešením puzzle.

    Puzzle tvoří jednotlivá slova na magnetických destičkách, která musí být uspořádána za sebou tak, aby poslední
    písmeno prvního slova, bylo prvním písmenem druhého atd.
    Př. Za slovem kolo může následovat ondatra dále pak ananas atd. Jednoduchý slovní fotbal.
    Použít se musí všechny destičky které na daných dveřích jsou.
    Pokud lze zadanou množinu slov takto uspořádat, řeší puzzle a odemyká dveře.

Vstupní data jsou pak uložena v souboru doors.txt:

    První řádek souboru je počet testovaných dveří (1-500).
    Následuje počet slov pro dané dveře (2-100000) = N
    A následně N řádků se slovy. Slova tvoří malá písmena anglické abecedy. Počet písmen 2 – 1000.
    Pak následuje počet slov pro druhé dveře atd.
"""
import codecs
from collections import defaultdict


def doors(file_name):
    """
    vrací iterable hodnot typu boolean určující funkčnost puzzle pro jednotlivé sady slov
    :param file: Vstupní soubor
    :return: ANO (True); NE (False)
    """
    return (_testit(words) for words in _get_wordlist(file_name))


def _get_wordlist(file_name):
    """
    Parse file by given pattern into several iterable lists of words
    """
    file = codecs.open(file_name, 'r', encoding='utf-8')
    for _s in range(int(file.__next__())):
        yield (file.__next__().strip() for _w in range(int(file.__next__())))


def _testit(words):
    """
    determines whether the puzzle opens doors
    """
    fl = defaultdict(lambda: [0, 0])
    for word in words:
        fl[word[0].lower()][0] += 1
        fl[word[-1].lower()][1] += 1
    lst = sorted([pair[0] - pair[1] for pair in fl.values()])
    return all(i == 0 for i in lst[1:-1]) and lst[-1] <= 1 and sum(lst[::len(lst) - 1]) == 0


if __name__ == "__main__":
    for i in doors("doors.txt"):
        print(i)
