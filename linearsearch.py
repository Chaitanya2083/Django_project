def linearsearch(myitem, mylist):
    found = False
    position = 0
    while position < len(mylist) and not found:
        if mylist[position] == myitem:
            found = True
            position = position + 1
        return found

    


