# -*- coding: utf-8 -*-
"""
Vytvorte funkce encrypt a decrypt pro Caesarovu sifru.
Kompletni zadani v elearningu.
"""
ALPHA = ''.join([chr(i) for i in range(97, 123)])


def encrypt(sentence, trans):
    """
    na vstupu přijme dva parametry - řetězec a offset a jako výstup vrátí
    nový řetězec.
    :param word - slovo k zasifrovani
    :param offset - znakovy posun
    :return: zasifrovane slovo
    """
    trans = trans % 26
    code = str.maketrans(ALPHA.upper()+ALPHA, ALPHA.upper()[trans:] +
                         ALPHA.upper()[:trans] + ALPHA[trans:] + ALPHA[:trans])
    return sentence.translate(code)


def decrypt(sentence, trans):
    """
    decrypt přijme řetězec a offset a vrátí řetězec původní.
    :param word - zasifrovane slovo
    :param offset - znakovy posun
    :return: desifrovane slovo
    """
    return encrypt(sentence, trans * (-1))

