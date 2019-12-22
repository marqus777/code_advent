from collections import Counter
from difflib import SequenceMatcher
import time
start_time = time.time()


def letters_counter(identifier):
    doubles = False
    triples = False
    id_as_counter = Counter(identifier)
    id_no_dup = set(identifier)
    print(id_no_dup)
    for letter in id_no_dup:
        print("Count: " + str(id_as_counter[letter]))
        if id_as_counter[letter] is 2:
            doubles = True
        elif id_as_counter[letter] is 3:
            triples = True
    return [doubles, triples]


doubles_counter = 0
triples_counter = 0

with open("input.txt", "r") as f:
    data = f.readlines()
    for index, first_string in enumerate(data):
        for another_string in data[index:]:
            similarity = SequenceMatcher(a=first_string, b=another_string).ratio()
            if 1.0 > similarity >= 0.96:
                print("{}{}{}\n".format(first_string, another_string, similarity))


print("--- %s seconds ---" % (time.time() - start_time))