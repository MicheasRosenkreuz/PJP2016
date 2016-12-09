# úkol 8. - karty na black jack

Znáte karetní hru Black Jack, česky též Voko bere? Dnešní úkol je vytvořit relativně jednoduchou třídu reprezentující karty pro tuto hru. A dále i příslušné testy pro jednotlivé metody

Třída **Card** bude reprezentovat hrací kartu pro hru Black Jack. Třídě implementujte následující metody a vlastnosti:

* Základní konstruktor **__init__(self, rank, suit)** - rank je hodnota karty od 1 do 13 (Eso - Král), suit je barva karty (srdce, kára, piky, trefy).
* pokud karta vytvořit nejde - například proto, že je špatná barva či hodnota, měla by třída vyhodit nějakou výjimku - nejlépe **TypeError**, eventuelně **ValueError**. Test pro vyhazování výjimek se vytváří za pomoci metody raises z modulu pytest. Dejte si pozor na to co jsme si na přednášce říkali o programování v konstruktoru.
* **rank(self)** - metoda která zpřístupní hodnotu karty jako číslo
* **suit(self)** - metoda která zpřístipní barvu karty jako písmeno s, k, p, t
* **black_jack_rank(self)** - vrátí hodnotu karty ve hře Black Jack - eso je jednička, ostatní figury (K, Q, J) jsou za 10 bodů. Zbylé karty mají hodnotu danou číslem.
* **__str__(self)** - hodnota i barva karty jako text - např. křížový král, srdcové eso, trefová dvojka atd. Konkrétní slova si můžete zvolit.
* na závěr implementujte operaci **porovnávání karet podle black_jack_rank** - budete potřebovat hned několik speciálních metod. Jakých?

Ke každé implementované metodě vytvořte test, který potvrdí, že metoda pracuje korektně. Testy umístěte do samostatného souboru **test_card.py**. Pro vytváření a spouštění testů doporučuji **py.test**, ale není to podmínka - můžete použít i doctest, unittest či nose.

**Testy jsou nutná součást řešení - pokud je nevytvoříte, máte max. 5 bodů.**

A  jako obvykle musí řešení splňovat tyto podmínky:

1. musí jít o testovatelný kód - vše tedy musí být buť ve funkcích, nebo uzavřeno pod __name__ == '__main__'
2. **modul musí být v adresáři cv08** a musí se jmenovat **card.py**. Soubor obsahující testy se musí jmenovat **test_card.py**.  Jako obvykle doporučuji využít kopii z repozitáře.
3. výsledný kód musí při testu programem PyLint se standardním nastavením získat alespoń 8 bodů. Za každý bod dolů, máte bod dolů i vy.
4. Můžete použít libovolné moduly ze standardní instalace Pythonu 3.5 a pochopitelně i doinstalovaný modul pro testy (pytest či nose).
