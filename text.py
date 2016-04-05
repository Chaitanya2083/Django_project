def binarysearch(myitem, mylist):
    found = False
    bottom = 0
    top = len(mylist)-1
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if mylist[middle] == myitem:
            found = True
        elif mylist[middle] < myitem:
            bottom = middle + 1
        else:
            top = middle - 1
        return found



#jhkjhkjhkjhkjhkjhkh

