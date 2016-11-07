# -*- coding: utf-8 -*-
"""
Py.test testy pro caesar
"""
import caesar


def test_caesar_encrypt_lower():
    """
    Test caesar lower
    """
    assert caesar.encrypt("the quick brown fox jumps over the lazy dog", 10) == "dro aesmu lbygx pyh tewzc yfob dro vkji nyq"


def test_caesar_encrypt_upper():
    """
    Test caesar upper
    """
    assert caesar.encrypt("the quick brown fox jumps over the lazy dog".upper(), 10) == "DRO AESMU LBYGX PYH TEWZC YFOB DRO VKJI NYQ"


def test_caesar_encrypt_mix():
    """
    Test caesar mix
    """
    assert caesar.encrypt("tHe QuiCk brOwn fox Jumps OVER ThE LaZy dog", 10) == "dRo AesMu lbYgx pyh Tewzc YFOB DrO VkJi nyq"


def test_caesar_encrypt_insane():
    """
    Test caesar insane
    """
    assert caesar.encrypt("the quick brown fox jumps over the lazy dog?", 500) == "znk waoiq hxuct lud pasvy ubkx znk rgfe jum?"


def test_caesar_decrypt_lower():
    """
    Test caesar lower
    """
    assert caesar.decrypt("dro aesmu lbygx pyh tewzc yfob dro vkji nyq", 10) == "the quick brown fox jumps over the lazy dog"


def test_caesar_decrypt_upper():
    """
    Test caesar upper
    """
    assert caesar.decrypt("DRO AESMU LBYGX PYH TEWZC YFOB DRO VKJI NYQ", 10) == "the quick brown fox jumps over the lazy dog".upper()


def test_caesar_decrypt_mix():
    """
    Test caesar mix
    """
    assert caesar.decrypt("dRo AesMu lbYgx pyh Tewzc YFOB DrO VkJi nyq", 10) == "tHe QuiCk brOwn fox Jumps OVER ThE LaZy dog"


def test_caesar_decrypt_insane():
    """
    Test caesar insane
    """
    assert caesar.decrypt("znk waoiq Hxuct lud_ pasvy ubkx znk rgFe jum?", 500) == "the quick Brown fox_ jumps over the laZy dog?"


def test_caesar_encrypt_zapor():
    """
    Test caesar zapor
    """
    assert caesar.encrypt("the quick Brown fox_ jumps over the laZy dog?", -500) == "nby kocwe Vliqh zir_ dogjm ipyl nby fuTs xia?"


def test_caesar_decrypt_zapor():
    """
    Test caesar zapor
    """
    assert caesar.decrypt("the quick Brown fox_ jumps over the laZy dog?", -500) == "znk waoiq Hxuct lud_ pasvy ubkx znk rgFe jum?"
