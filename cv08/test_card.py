"""
testy
"""
import pytest
from card import Card

CARD1 = Card(5, 2)
CARD2 = Card(3, 3)
CARD3 = Card(3, 1)
CARD4 = Card(5, 2)

def test_raise1():
    with pytest.raises(ValueError):
        Card(1, -1)


def test_raise2():
    with pytest.raises(ValueError):
        Card(15, 0)

def test_type():
    # assert type(Card(1, 1)) == Card
    assert isinstance(Card(1, 1), Card)

def test_int():
    assert int(CARD1) == 5

def test_cmp():
    assert CARD1 != CARD2
    assert CARD2 == CARD2
    assert CARD3 <= CARD2
    assert CARD3 >= CARD2
    assert CARD3 < CARD1
    assert CARD1 > CARD2

    # duvod proc v comparatorech porovnavam int(other) a ne other.__value
    assert CARD1 == 5
    assert CARD1 != 50
    assert CARD3 > 1
    assert CARD3 >= 1
    assert CARD3 < 10
    assert CARD3 <= 10


def test_hash():
    """
    CARD4 a CARD1 mají stejný hash díky __hash__()
    """
    st = {CARD1, CARD2, CARD3}
    assert CARD4 in st

def test_methods():
    assert CARD1.black_jack_rank() == 5
    assert CARD1.rank() == 5
    assert CARD1.suit() == 'k'
