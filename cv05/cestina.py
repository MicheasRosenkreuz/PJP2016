# -*- coding: utf-8 -*-
"""
@author: Michal Jirasek
Modul pro ukol 5
"""
import re
# split_text = lambda x: re.findall(r'\w+\-\w+|\w+', x)


def split_text(text):
    """
    Vrátí seznam slov bez interpunkčních znamének.
    """
    return re.findall(r'\w+\-\w+|\w+', text)
