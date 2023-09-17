def only_ints(dew, aew):
    if not(isinstance(dew, int) and isinstance(aew, int)):
        print(bool(False))

    elif (isinstance(dew, bool) or isinstance(aew, bool)):
        print(bool(False))

    else:
        print(bool(True))
only_ints(1, 2)






 