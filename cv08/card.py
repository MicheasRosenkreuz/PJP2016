"""
@TODO implementujte dle zadání cvičení 8
"""


class Card(object):
    # _deck = list()
    _ranks = {**{1: {'value': 1, 'rank': 'ESO', "rod": 0},
                 11: {'value': 10, 'rank': 'K', "rod": 0},
                 12: {'value': 10, 'rank': 'Q', "rod": 0},
                 13: {'value': 10, 'rank': 'J', "rod": 0}},
              **{val: {'value': val, 'rank': str(val), "rod": 1}
                 for val in range(2, 11)}}
    _suits = {1: 's', 2: 'k', 3: 'p', 4: 't'}
    _suits_name = {0: {1: 'srdcové', 2: 'kárové', 3: 'pikové', 4: 'trefové'},
                   1: {1: 'srdcová', 2: 'kárová', 3: 'piková', 4: 'trefová'},
                   2: {1: 'srdcový', 2: 'kárový', 3: 'pikový', 4: 'trefový'}
                   }

    # pri chybe misto instance vrátí string "Kapradí"
    # def __new__(cls, *args, **kwargs):
    #     rank, suit = args
    #     if not (0 < rank < 14) or not (0 < suit < 5):
    #         return "Kapradí"
    #     return super(Card, cls).__new__(cls)

    def __init__(self, rank, suit):
        if not (0 < rank < 14) or not (0 < suit < 5):
            raise ValueError
        self._rank = rank
        self._suit = suit
        # tyhle promenny zaberou par bytu v pameti, ale zprehledni kod
        self.__suit_code = Card._suits[self._suit]
        self.__value = Card._ranks[self._rank]['value']
        self.__suit_name = Card._ranks[self._rank]['rod']
        # instance register
        # Card._deck.append(self)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __hash__(self):
        return int(str(self._rank) + str(self._suit))

    def __add__(self, other):
        return int(self) + int(other)

    def __int__(self):
        return self.__value

    def __str__(self):
        return Card._suits_name[self.__suit_name][self._suit] + \
               ' ' + Card._ranks[self._rank]['rank']

    def __repr__(self):
        return 'Card< ' + Card._ranks[self._rank]['rank'] + ', ' + \
               self.__suit_code + ' >(' + str(self.__value) + ')'

    def rank(self):
        return self._rank

    def suit(self):
        return self.__suit_code

    def black_jack_rank(self):
        return self.__value


if __name__ == "__main__":
    # for s in range(1, 5):
    #     for r in range(1, 14):
    #         print(Card(r, s))
    c1 = Card(2, 1)
    c2 = Card(2, 1)
    c3 = Card(11, 2)
    s = {c2, c3}
    # c1 a c2 mají stejnej hash díky __hash__()
    print("c1 in s", c1 in s)
    # duvod proc v comparatorech porovnavam int(other) a ne other.__value
    print("c1==2", c1==2)
    print("c1!=c2", c1!=c2)
    print("c1<c2", c1<c2)
    print("c1<=c2", c1<=c2)
    print("c1>c2", c1>c2)
    print("c1>=c2", c1>=c2)
