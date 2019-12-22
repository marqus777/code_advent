import copy
import re

reg_id = "(?<=#)\d*"
reg_x = "\d*(?=,\d*: \d*x\d*)"
reg_y = "\d*(?=: \d*x\d*)"
reg_width = "\d*(?=x\d*)"
reg_height = "(?<=\dx)\d*"


with open("input.txt", "r") as data:
    s = list(str(data.read()).rstrip("\n"))
    cont = True
    print(s)
    place = 0
    while cont:
        size = len(s)
        for index in range(place, size):
            actual_letter = s[index]
            try:
                next_letter = s[index + 1]
            except IndexError:
                print("{} {}".format(index, index+1))
            if actual_letter != next_letter and (actual_letter == next_letter.upper() or actual_letter.upper() == next_letter):
                print("Deleting: {} {}".format(s[index], s[index+1]))
                del s[index:index + 2]
                place = index - 1
                if place < 0:
                    place = 0
                break
            # print("{} {}".format(index-2, len(s)))
            if index+1 == size:
                print("Stop")
                cont = False
                break
    print(s)
    print(len(s))
