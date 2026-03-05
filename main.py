final = []
list.sort(random)
levelold = 0
openbrac = 0
closebrac = 0

for func in random:
    level = int(len(func) / 2 - 1)
    if(levelold < level):
        final.append('(')
        openbrac += 1
    elif(levelold > level):
        for i in range(0, levelold - level):
            final.append(')')
            closebrac += 1
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
    level = int(len(func) / 2 - 1)
    if(levelold < level):
        final.append('(')
        openbrac += 1
    elif(levelold > level):
        for i in range(0, levelold - level):
            final.append(')')
            closebrac += 1
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    elif(levelold == level):
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    final.append(func)

    levelold = level
            final.append('*')
    elif(levelold == level):
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    level = int(len(func) / 2 - 1)
    if(levelold < level):
        final.append('(')
        openbrac += 1
    elif(levelold > level):
        for i in range(0, levelold - level):
            final.append(')')
            closebrac += 1
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    elif(levelold == level):
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    final.append(func)

    levelold = level
    final.append(func)

    level = int(len(func) / 2 - 1)
    if(levelold < level):
        final.append('(')
        openbrac += 1
    elif(levelold > level):
        for i in range(0, levelold - level):
            final.append(')')
            closebrac += 1
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
    level = int(len(func) / 2 - 1)
    if(levelold < level):
        final.append('(')
        openbrac += 1
    elif(levelold > level):
        for i in range(0, levelold - level):
            final.append(')')
            closebrac += 1
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    elif(levelold == level):
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    final.append(func)

    levelold = level
            final.append('*')
    elif(levelold == level):
        if(func[2 * level + 1] <= '1'):
            final.append('+')
        else:
            final.append('*')
    final.append(func)

    levelold = level
    levelold = level

# FIXME: Find a way to handle functions in exponentials Ex: f1^(f2+f3)

for i in range(0, openbrac - closebrac):
    final.append(')')
eqstring = ""
for func in final:
    eqstring += str(func)

print(eqstring)
