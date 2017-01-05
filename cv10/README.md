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