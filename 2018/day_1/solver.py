
def scan_data():
    freq = 0
    freq_history = [0]
    keep_going = True
    while keep_going:
        for number in open("input.txt", "r"):
            print("number: " + str(number))
            freq += int(number)
            if freq in freq_history:
                return str(freq)
            else:
                freq_history.append(freq)
            print(freq)
        print("keep going")


print("Solution: " + scan_data())
