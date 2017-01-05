'''
Poslední úkol je jedno ze starších zkouškových zadání. Můžete si tedy vyzkoušet,
 jak vám to asi půjde.

U zkoušky máte k dispozici 150 minut času a můžete použít libovolnou literaturu.
 Programuje se na počítači. Můžete použít i vlastní notebook.

Úlohu musíte řešit samostatně a řešení pak následně obhájit.

A teď již to samotné zadání:

Úkolem je vytvořit modul pro odfiltrování zadaných slov z textu. Tedy jednoduchý
 cenzorovací systém.

Vstupem do programu jsou dva soubory. První z nich je HTML stránka obsahující text,
 který je potřeba profiltrovat. Druhý soubor obsahuje seznam zakázaných slov v jednoduchém
 formátu 1 slovo = 1 řádek.

Program  musí být možné  ovládat argumenty z příkazové řádky.

Ovládání programu musí zvládnou následující parametry:

    -i, --input : soubor který má být upraven (běžný text)
    -l, --list : soubor se seznamem zakázaných slov - jedno slovo jeden řádek
    -c, --clean : přepínač vyčištění souboru od html - viz. dále
    -o, --output: výstupní soubor, pokud není volba použita, tak vypsat data na obrazovku
    -h, --help : nápověda - o čem program je a jak se ovládá

Požadované vlastnosti:

    Pokud je skript spuštěn s parameterm -c (--clean) tak odstranit z textu všechny HTML
     značky - to znamená na výstup pouze text.
    Nahradit všechna zakázaná slova v textu sekvencí znaků #. Délka nahrazené sekvence musí
     být rovná délce původního (nahrazeného) slova.
    Pokud bude program spuštěn s parametrem -o jméno, vypsat výstup do souboru jméno.
     Jinak vypisovat na obrazovku.

Slova v textu: pro dělení slov můžete použít váš modul z předchozího úkolu (č.5).

HTML značky: jsou formátovací sekvence HTML. Od běžného textu jsou odděleny znaky < a >.

A obvyklé požadavky pro odezdání:

    musí jít o testovatelný kód - vše tedy musí být buť ve funkcích, nebo uzavřeno
     pod __name__ == '__main__'
    pro každou funkci, nebo metodu, kterou vytvoříte musí být v souboru test_censor.py
     alespoň jeden test. Testy budou spouštěny pomocí py.test skriptu.
    modul musí být v adresáři cv10 a musí se jmenovat censor.py.  Tady samozřejmě opět
     doporučuji využít kopii z repozitáře.
    výsledný kód musí při testu programem PyLint se standardním nastavením získat
     alespoń 8 bodů. Za každý bod dolů, máte bod dolů i vy.
    Pro řešení můžete použít libovolný built-in balíček z Pythonu 3.5.

@author = Frantisek Jukl
'''

import sys
import argparse
import codecs
import re
import os

def argument_parser(argv):
    '''
    communication with user
    parsing arguments
    return input, output, list files
    '''
    parser = argparse.ArgumentParser(description="Censor that like in KLDR",\
    epilog="And that's how we do it",\
    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-i", "--input", required=True, metavar="FILE",\
     help="input file ready for cleaning")
    parser.add_argument("-l", "--list", required=True, metavar="FILE",\
     help="list of banned words, make them all Aladin")
    parser.add_argument("-c", "--clean", required=True, action="store_true",\
     help="cleaning service")
    parser.add_argument("-o", "--output", required=False, metavar="FILE",\
     help='''save the words for the news\nif not specified, publish it on tv''')
    args = parser.parse_args(argv)
    return args.input, args.list, args.output if args.output is not None else False

def clean_tags(finput):
    '''
    clean html tags from finput file
    return stripped clean text
    '''
    try:
        with codecs.open(finput, 'r') as fil:
            fread = fil.read()
        return os.linesep.join(list(filter(None, re.sub("<[^>]*>", "", fread)\
        .strip().splitlines())))
    except FileNotFoundError as err:
        print(err)
        sys.exit(2)

def clean_banned_words(flist, text):
    '''
    read and sub banned words
    return text with # instead of words
    '''
    try:
        with codecs.open(flist, 'r') as fil:
            words = fil.read().split()
        for word in words:
            text = re.sub(word, "#"*len(word), text, flags=re.IGNORECASE)
        return text
    except FileNotFoundError as err:
        print(err)
        sys.exit(2)

def write_output(foutput, text):
    '''
    write text to file
    '''
    with codecs.open(foutput, 'w', encoding='utf8') as fil:
        fil.write(text)

def main(argv):
    '''
    get files - get text - decide for printing to file/terminal
    '''
    finput, flist, foutput = argument_parser(argv[1:])
    result = clean_banned_words(flist, clean_tags(finput))
    if foutput:
        write_output(foutput, result)
    else:
        print(result)

if __name__ == "__main__":
    main(sys.argv)
