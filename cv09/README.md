# Úkol 9. - zpracování HTML dokumentů

Na adrese [http://www.nti.tul.cz/~vrany/pjp_data/](http://www.nti.tul.cz/~vrany/pjp_data/) najdete několik html dokumentů, navzájem propojených odkazy. Kořenem této struktury je soubor index.html. V dokumentech se v různé formě vyskytují e-mailové adresy. Některé jsou přímo vidět, jiné jsou trochu schované.

**Cílem cvičení je vytvořit program, který dokáže najít co nejvíc těchto adres.** 

Při výpadku www.nti.tul.cz můžete použít alternativní kopii zdrojových dat na [https://jirivrany.github.io/pjp_html_data/](https://jirivrany.github.io/pjp_html_data/)

Váš vysledný program musí vyřešit následující úkoly:

* **Zjistit kolik dokumentů** tvoří prohledávanou množinu. Dokumenty jsou propojené navzájem odkazy, ale mohou obsahovat také odkazy na jiný server. Tyto odkazy jinam musí váš program vynechat a nesledovat je. 
* **Množinu** prohledávaných dokumentů uložit **ve formě indexu (dictionary) odkazů**. Požadovaná struktura indexu je následující:

```python
{
'soubor.html' : ['1.html', '2.html'], 
'soubor2.html' : ['3.html', '2.html']
}
```
Jméno souboru jako klíč a odkazované soubory jako položky listu pod tímto klíčem.
* Konečně - prohledat všechny nalezené dokumenty a **najít** v nich pokud možno **všechny e-mailové adresy**. Adresy jsou různě ukryté a obsahují také pokusy o jednoduchý anti-spam a obfuskaci. Pravidla pro hledání :
    * Platný e-mail může obsahovat pouze malá písmena, číslice a znak @. Ostatní znaky pokud se vyskytují jsou anti-spam a program by je měl odstranit.
    * Některé adresy jsou aktivní odkazy, ale ne všechny.
    * Některé obsahují základní pokusy o antispam
* **Výsledky** musí program **zapsat do souboru** scrap_result.txt v tomto formátu: nejprve nalezený index, následně volný řádek a pak už jednotlivé e-maily, každý na nový řádek.

**Pro kontrolu**: ať si to nemusíte ručně počítat sami. Soubory jsou celkem 4 a adres je v nich různým způsobem ukryto celkem 7. Pro nalezení všech musíte zkombinovat několik různých způsobů hledání. Program ale samozřejmě musí být univerzální, to znamená, že musí zvládnou situaci, kdy bude za stejných pravidel přidán další soubor a další adresy.

**Řešení musí samozřejmě splňovat obvyklá pravidla:**

1. Musí jít o testovatelný kód - vše tedy musí být buť ve funkcích, nebo uzavřeno pod `__name__ == '__main__'`
2. Modul musí být v adresáři cv09, musí se jmenovat scraper.py a výsledný soubor se musí jmenovat scrap_result.txt. Jako obvykle najdete šablonu ve vzorovém repozitáři.  
3. Pro řešení vám musí stačit standardní instalace Pythonu (bez balíčků třetích stran). Nemůžete tedy použít například moduly BeautifulSoup či Requests.
4. Výsledný kód musí při testu programem PyLint se standardním nastavením získat alespoń 8 bodů. Za každý bod dolů, máte bod dolů i vy.
5. Řešení jako obvykle odevzdejte pomocí gitu do svého repositáře na gitlab.tul.cz.
