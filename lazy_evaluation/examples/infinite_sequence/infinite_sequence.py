def infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1


for item in infinite_sequence():
    if item > 100:
        break
    # Do something here
