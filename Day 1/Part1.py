def calibration(mot):
    first = ""
    last = ""
    for i in range(len(mot)):
        if first == "":
            try:
                first = int(mot[i])
            except Exception as e:
                None
        else:
            try:
                last = int(mot[i])
            except Exception as e:
                None
        if last == "":
            last = first
    somme = int(str(first) + str(last))
    return somme


data = open('input.txt').read().splitlines()
somme = 0

for i in range(len(data)):
    somme += calibration(data[i])

print(somme)
