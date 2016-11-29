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


def doors(file_name):
    """
    vrací iterable hodnot typu boolean určující funkčnost puzzle pro jednotlivé
    sady slov
    :param file: Vstupní soubor
    :return: ANO (True); NE (False)
    """
    return (_testit(words) for words in _get_wordlist(file_name))


def _get_wordlist(file_name):
    """
    Parse file by given pattern into several iterable lists of words
    """
    ifile = codecs.open(file_name, 'r', encoding='utf-8')
    for _ in range(int(ifile.__next__())):
        yield (ifile.__next__().strip() for _w in range(int(ifile.__next__())))


def _testit(words):
    """
    determines whether the puzzle opens doors
    """
    pairs = defaultdict(lambda: [0, 0])
    for word in words:
        pairs[word[0].lower()][0] += 1
        pairs[word[-1].lower()][1] += 1
    lst = sorted([pair[0] - pair[1] for pair in pairs.values()])
    return all(i == 0 for i in lst[1:-1]) and \
        lst[-1] <= 1 and sum(lst[::len(lst) - 1]) == 0

def jedna_komponenta(slova):
    """
    zjisti, zda se slova skladaj z jedne souvisle komponenty
    input list slova
    return True - jedna komponenta
    return False - vice komponent
    """
    # pouze unikatni slova, cyklovy list
    slova1 = list(set(slova))
    # nastaveni pracovniho listu pro mazani prvku
    slova2 = list(slova1)
    prvni_pismena = []
    posledni_pismena = []
    index = 0
    aktual = slova1[0]
    slova2.remove(aktual)
    prvni_pismena.append(aktual[:1])
    posledni_pismena.append(aktual[-1:])
    # cyklus jede, pokud nejsou pouzity vsechny prvky v listech prvnich a poslednich pismen
    # pro kazdy prvek zjisti, zda existuje takove slovo, na ktere lze navazat
    # lze na slovo navazat pokud: prvni_pismeno == posledni pismeno slova
    # nebo posledni_pismeno == prvni pismeno slova
    # z tohoto slova se ulozi prvni a posledni pismena do listu, pokud tam jiz nejsou
    # slovo se smaze z pracovniho listu
    # zvysi se index pro dalsi prochazeni whilu
    while index < len(prvni_pismena) or index < len(posledni_pismena):
        aktual_prvni = prvni_pismena[index] if index < len(prvni_pismena) else ''
        aktual_posledni = posledni_pismena[index] if index < len(posledni_pismena) else ''
        for slovo in slova1:
            if slovo[:1] == aktual_posledni or slovo[-1:] == aktual_prvni:
                if slovo[:1] not in prvni_pismena:
                    prvni_pismena.append(slovo[:1])
                if slovo[-1:] not in posledni_pismena:
                    posledni_pismena.append(slovo[-1:])
                if slovo in slova2:
                    slova2.remove(slovo)
        index += 1
    return True if len(slova2) == 0 else False

if __name__ == "__main__":
    for i in doors("_d2.txt"):
        print(i)
