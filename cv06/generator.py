# -*- coding: utf-8 -*-
import codecs
import random as rnd
import sys

if __name__ == '__main__':
    # filename = 'doors.txt'
    # w_count = 10
    if len(sys.argv) == 3:
        w_count = int(sys.argv[1])
        filename = sys.argv[2]
    else:
        sys.exit("Usage: generator <locks num> <filename>")
    original = codecs.open('wordlist.txt', 'r', encoding='utf-8')
    word_tree = {}
    for _w in original:
        if not _w[0].lower() in word_tree:
            word_tree[_w[0].lower()] = [_w.strip(), ]
        word_tree[_w[0].lower()].append(_w.strip())

    false = False
    last = chr(rnd.randrange(97, 122))
    out_list = []
    for _i in range(w_count):
        _word = rnd.choice(word_tree[last])
        out_list.append(_word + '\n')
        if _word[-1] not in word_tree:
            false = True
            continue
        last = _word[-1]
    rnd.shuffle(out_list)
    if false:
        filename = "false_" + filename
    out_file = codecs.open(filename, mode='w', encoding='utf-8')
    out_file.write(str(w_count) + '\n')
    out_file.writelines(out_list)
    sys.exit(filename + " created")
