base = input("Please enter a number:\n")

prevnumber = base
nextnumber = float(prevnumber) + float(base)

for x in range(0, 19):
    print("Below is time %d" % (x+2))
    nextnumber = float(prevnumber) + float(base)
    prevnumber = nextnumber
    printnumber = nextnumber
    print(nextnumber)


