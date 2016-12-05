# -*- coding: utf-8 -*-
"""
Motivace: dveře jsou uzavřeny speciálním druhem zámku, který se otevírá
vyřešením puzzle.

    Puzzle tvoří jednotlivá slova na magnetických destičkách, která musí být
    uspořádána za sebou tak, aby poslední
    písmeno prvního slova, bylo prvním písmenem druhého atd.
    Př. Za slovem kolo může následovat ondatra dále pak ananas atd.
    Jednoduchý slovní fotbal.
    Použít se musí všechny destičky které na daných dveřích jsou.
    Pokud lze zadanou množinu slov takto uspořádat, řeší puzzle a odemyká dveře.

Vstupní data jsou pak uložena v souboru doors.txt:

    První řádek souboru je počet testovaných dveří (1-500).
    Následuje počet slov pro dané dveře (2-100000) = N
    A následně N řádků se slovy. Slova tvoří malá písmena anglické abecedy.
    Počet písmen 2 – 1000.
    Pak následuje počet slov pro druhé dveře atd.
"""
import codecs
from collections import defaultdict
from copy import copy
__author__ = "Michal Jirásek"
__email__ = "michal.jirasek@tul.cz"
__credits__ = "Frantisek Jukl (Antoninecek)"


def doors(file_name, test=None):
    """
    vrací iterable hodnot typu boolean určující funkčnost puzzle pro jednotlivé
    sady slov
    :param file: Vstupní soubor
    :return: ANO (True); NE (False)
    """
    if test is None:
        test = _testit
    return (test(words) for words in _get_wordlist(file_name))


def _get_wordlist(file_name):
    """
    Parse file by given pattern into several iterable lists of words
    """
    ifile = codecs.open(file_name, 'r', encoding='utf-8')
    for _ in range(int(ifile.__next__())):
        yield (ifile.__next__().strip() for _ in range(int(ifile.__next__())))


def _testit(words):
    """
    determines whether the puzzle opens doors
    """
    w_list = list(words)
    pairs = defaultdict(lambda: [0, 0])
    if not _is_component(w_list):
        return False
    for word in w_list:
        pairs[word[0].lower()][0] += 1
        pairs[word[-1].lower()][1] += 1
    lst = sorted([pair[0] - pair[1] for pair in pairs.values()])
    return all(i == 0 for i in lst[1:-1]) and \
           lst[-1] <= 1 and sum(lst[::len(lst) - 1]) == 0


def _alternative(words):
    """
    My version of algorithm for hamiltonian path problem.
    Searching all permutation of graph nodes.
    Really slow algorithm: O(n**2*2**n).
    """
    wordlist = list(words)
    counter = []
    for word in wordlist:
        used = set()
        counter.append(__geterate_tree(word, wordlist, used, 1))
    return max(counter) == len(wordlist)


def __geterate_tree(word, wordlist, used, length):
    used.add(word)
    counter = []
    for _word in (w for w in wordlist if w.startswith(word[-1])):
        if _word not in used and _word is not None:
            counter.append(
                __geterate_tree(_word, wordlist, copy(used), length + 1))
    if counter:
        return max(counter)
    return length


def _is_component(words):
    """
    @author = "Frantisek Jukl (Antoninecek)"
    zjisti, zda se slova skladaj z jedne souvisle komponenty
    input list slova
    return True - jedna komponenta
    return False - vice komponent
    """
    init_word = words[0]
    words = set(words)  # odstrani duplicity
    seen = {init_word, }
    first_ch = {init_word[0], }
    last_ch = {init_word[-1], }
    index = 0
    while index < max(len(first_ch), len(last_ch)):
        for word in words:
            if word[:1] in last_ch or word[-1:] in first_ch:
                first_ch.add(word[:1])
                last_ch.add(word[-1:])
                seen.add(word)
        index += 1
    return len(seen) == len(words)


if __name__ == "__main__":
    print(list(doors("doors.txt")))
