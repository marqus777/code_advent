import copy
import re

reg_id = "(?<=#)\d*"
reg_x = "\d*(?=,\d*: \d*x\d*)"
reg_y = "\d*(?=: \d*x\d*)"
reg_width = "\d*(?=x\d*)"
reg_height = "(?<=\dx)\d*"


with open("input.txt", "r") as data:
    ilosc = 0
    takie_same = 0
    o = data.readlines()
    for scrap in o:
        # print("Teraz: " + str(scrap))
        b = copy.deepcopy(o)
        scrap_id = int(re.search(reg_id, scrap).group(0))
        scrap_x = int(re.search(reg_x, scrap).group(0))
        scrap_y = int(re.search(reg_y, scrap).group(0))
        scrap_width = int(re.search(reg_width, scrap).group(0))
        scrap_height = int(re.search(reg_height, scrap).group(0))
        s_width = range(scrap_x, scrap_x + scrap_width)
        s_height = range(scrap_y, scrap_y + scrap_height)
        fine = True
        number_of_loops = 0
        for el in o:
            ilosc += 1
            if fine:
                el_scrap_id = int(re.search(reg_id, el).group(0))
                el_scrap_x = int(re.search(reg_x, el).group(0))
                el_scrap_y = int(re.search(reg_y, el).group(0))
                el_scrap_width = int(re.search(reg_width, el).group(0))
                el_scrap_height = int(re.search(reg_height, el).group(0))
                el_width = range(el_scrap_x, el_scrap_x + el_scrap_width)
                el_height = range(el_scrap_y, el_scrap_y + el_scrap_height)
                el_scrap_squares = []
                if int(el_scrap_id) == int(scrap_id):
                    continue
                for a in s_width:
                    if fine:
                        for b in s_height:
                            # print(str(a)+","+str(b)+" in "+str(el_width)+" "+str(el_height))
                            if (a in el_width) and (b in el_height):
                                # print("Wspolne")
                                fine = False
                                break
                    else:
                        break
                number_of_loops += 1

        if fine:
            print("Win: " + str(scrap_id) + " number of loops: " + str(number_of_loops))
    print("Repeatitions: " + str(ilosc))
    print("Takie same: " + str(takie_same))


