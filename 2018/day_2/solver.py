from collections import Counter


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

with open("input.txt", "r") as data:
    for number in data:
        result = letters_counter(number)
        if result[0]:
            doubles_counter += 1
        if result[1]:
            triples_counter += 1
    print("{} * {} = {}".format(doubles_counter, triples_counter, doubles_counter * triples_counter))
