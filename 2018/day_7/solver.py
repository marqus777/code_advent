import numpy as np
from scipy.spatial import distance
import string

import re

reg = "(?<= )\D(?= )"

workpath = []

with open("input", "r") as data:
    sent = [l for l in data.read().splitlines()]
    for i in range(10):
        for l in sent:
            let_pair = re.findall(reg, l)
            # print(let_pair[0], let_pair[1])
            letter1 = let_pair[0]
            letter2 = let_pair[1]
            if len(workpath) == 0:
                workpath.extend([letter1, letter2])
            if letter1 in workpath:
                letter1_loc = workpath.index(letter1)
                if letter2 in workpath:
                    letter2_loc = workpath.index(letter2)
                    if letter1_loc > letter2_loc:
                        for a in workpath[letter1_loc + 1:]:
                            if string.ascii_uppercase.index(a) > string.ascii_uppercase.index(letter2):
                                workpath.insert(workpath.index(a), letter2)
                                break
                            elif workpath[-1] == a:
                                workpath.append(letter2)
                                break
                        del workpath[letter2_loc]
                elif letter2 not in workpath:
                    for a in workpath[letter1_loc+1:]:
                        if string.ascii_uppercase.index(a) > string.ascii_uppercase.index(letter2):
                            workpath.insert(workpath.index(a), letter2)
                            break
                        elif workpath[-1] == a:
                            workpath.append(letter2)
                            break
            elif letter1 not in workpath:
                if letter2 not in workpath:
                    continue
                elif letter2 in workpath:
                    letter2_loc = workpath.index(letter2)
                    workpath.insert(letter2_loc, letter1)


        print(str(''.join(workpath)))


