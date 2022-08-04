def mysplit(strng):
    if strng =='' or strng.isspace():
        return [ ]
    list = []
    word = ''
    inword = not strng[0].isspace()
    for x in strng:
        if inword:
            if not x.isspace ():
               word = word + x
            else:
                list.append(word)
                inworld = False
        else:
            if not x.isspace():
                inword = True
                word = x
            else:
                pass
    if inword:
       list.append(word)
    return list

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))