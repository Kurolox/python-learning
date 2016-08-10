string = list(input())
loopstart = string.index("[")
loopend = string.index("]")
flag = True
while flag:
    newstring = string[(loopstart+1):loopend]
    if "[" in newstring:
        multnumber = newstring.count("[")
        print (multnumber)
        loopstart = string.index("[")
        loopend = string.index("]", (loopend+1))
    else:
        flag = False
print (newstring)
