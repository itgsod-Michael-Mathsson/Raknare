def count(start, stop):
    counter = str(start)
    if start < stop:
        while start < stop:
            start = start + 1
            counter = counter + "," + str(start)
        return counter
    elif stop < start:
        while stop < start:
            start = start -1
            counter = counter + "," + str(start)
        return counter
    else:
        return counter

print count(-5, 6)

